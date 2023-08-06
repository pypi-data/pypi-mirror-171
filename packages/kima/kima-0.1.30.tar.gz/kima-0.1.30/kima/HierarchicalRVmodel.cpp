#include "HierarchicalRVmodel.h"

#define TIMING false

const double halflog2pi = 0.5*log(2.*M_PI);


/* set default priors if the user didn't change them */

void HierarchicalRVmodel::setPriors()  // BUG: should be done by only one thread!
{
    betaprior = make_prior<Gaussian>(0, 1);

    if (!Cprior)
        Cprior = make_prior<Uniform>(data.get_RV_min(), data.get_RV_max());

    if (!Jprior)
        Jprior = make_prior<ModifiedLogUniform>(1, 10);

    if (trend){
        if (degree == 0)
            throw std::logic_error("trend=true but degree=0");
        if (degree > 3)
            throw std::range_error("can't go higher than 3rd degree trends");
        if (degree >= 1 && !slope_prior)
            slope_prior = make_prior<Gaussian>( 0.0, pow(10, data.get_trend_magnitude(1)) );
        if (degree >= 2 && !quadr_prior)
            quadr_prior = make_prior<Gaussian>( 0.0, pow(10, data.get_trend_magnitude(2)) );
        if (degree == 3 && !cubic_prior)
            cubic_prior = make_prior<Gaussian>( 0.0, pow(10, data.get_trend_magnitude(3)) );
    }

    // if offsets_prior is not (re)defined, assume a default
    if (data.datamulti && !offsets_prior)
        offsets_prior = make_prior<Uniform>( -data.get_RV_span(), data.get_RV_span() );

    for (size_t j = 0; j < data.number_instruments - 1; j++)
    {
        // if individual_offset_prior is not (re)defined, assume a offsets_prior
        if (!individual_offset_prior[j])
            individual_offset_prior[j] = offsets_prior;
    }

    if (known_object) { // KO mode!
        // if (n_known_object == 0) cout << "Warning: `known_object` is true, but `n_known_object` is set to 0";
        for (int i = 0; i < n_known_object; i++){
            if (!KO_Pprior[i] || !KO_Kprior[i] || !KO_eprior[i] || !KO_phiprior[i] || !KO_wprior[i])
                throw std::logic_error("When known_object=true, please set priors for each (KO_Pprior, KO_Kprior, KO_eprior, KO_phiprior, KO_wprior)");
        }
    }

    if (studentt)
        nu_prior = make_prior<LogUniform>(2, 1000);

}


void HierarchicalRVmodel::from_prior(RNG& rng)
{
    // preliminaries
    setPriors();
    save_setup();

    for (size_t i = 0; i < data.Ns(); i++)
        mu[i].resize(data.Neach[i]);

    for (auto &&p : planets)
    {
        p.from_prior(rng);
        p.consolidate_diff();
    }
    

    for (auto &&b : background)
        b = Cprior->generate(rng);
    

    if(data.datamulti)
    {
        for(int i=0; i<offsets.size(); i++)
            offsets[i] = individual_offset_prior[i]->generate(rng);
        for(int i=0; i<jitters.size(); i++)
            jitters[i] = Jprior->generate(rng);
    }
    else
    {
        extra_sigma = Jprior->generate(rng);
    }


    if(trend)
    {
        if (degree >= 1) slope = slope_prior->generate(rng);
        if (degree >= 2) quadr = quadr_prior->generate(rng);
        if (degree == 3) cubic = cubic_prior->generate(rng);
    }

    if (known_object) { // KO mode!
        KO_P.resize(n_known_object);
        KO_K.resize(n_known_object);
        KO_e.resize(n_known_object);
        KO_phi.resize(n_known_object);
        KO_w.resize(n_known_object);

        for (int i=0; i<n_known_object; i++){
            KO_P[i] = KO_Pprior[i]->generate(rng);
            KO_K[i] = KO_Kprior[i]->generate(rng);
            KO_e[i] = KO_eprior[i]->generate(rng);
            KO_phi[i] = KO_phiprior[i]->generate(rng);
            KO_w[i] = KO_wprior[i]->generate(rng);
        }
    }

    if (studentt)
        nu = nu_prior->generate(rng);

    calculate_mu();
}

/**
 * @brief Calculate the full RV model
 * 
*/
void HierarchicalRVmodel::calculate_mu()
{
    size_t Ns = data.Ns();

    #if TIMING
    auto begin = std::chrono::high_resolution_clock::now();  // start timing
    #endif

    for (size_t i = 0; i < Ns; i++)
    {
        size_t N = data.Neach[i];

        // Update or from scratch?
        bool update = (planets[i].get_added().size() < planets[i].get_components().size()) &&
                      (staleness <= 10);
        // Get the components
        const vector<vector<double>> &components = (update) ? (planets[i].get_added()) : (planets[i].get_components());
        // at this point, components has:
        //  if updating: only the added planets' parameters
        //  if from scratch: all the planets' parameters

        // Zero the signal
        if(!update) // not updating, means recalculate everything
        {
            mu[i].assign(mu[i].size(), background[i]);
            
            staleness = 0;

            // if(trend)
            // {
            //     double tmid = data.get_t_middle();
            //     for(size_t i=0; i<N; i++)
            //     {
            //         mu[i] += slope * (data.t[i] - tmid) +
            //                  quadr * pow(data.t[i] - tmid, 2) +
            //                  cubic * pow(data.t[i] - tmid, 3);
            //     }
            // }

            // if(data.datamulti)
            // {
            //     for(size_t j=0; j<offsets.size(); j++)
            //     {
            //         for(size_t i=0; i<N; i++)
            //         {
            //             if (data.obsi[i] == j+1) { mu[i] += offsets[j]; }
            //         }
            //     }
            // }

            if (known_object) { // KO mode!
                add_known_object();
            }
        }
        else // just updating (adding) planets
            staleness++;


        double f, v, ti;
        double P, K, phi, ecc, omega, Tp;
        for (size_t j = 0; j < components.size(); j++)
        {
            if (false) // hyperpriors
                P = exp(components[j][0]);
            else
                P = components[j][0];

            K = components[j][1];
            phi = components[j][2];
            ecc = components[j][3];
            omega = components[j][4];

            auto v = brandt::keplerian(data.t[i], P, K, ecc, omega, phi, data.M0_epoch);
            for (size_t k = 0; k < N; k++)
                mu[i][k] += v[k];
        }
    }

    for (size_t i = 0; i < data.Ns(); i++)
    {
        int k = 0;
        for (size_t j = 0; j < data.N(); j++)
        {
            if (data.ijoin[j] == i) {
                mujoin[j] = mu[i][k];
                k++;
            }
        }
    }
    
    // #if TIMING
    // auto end = std::chrono::high_resolution_clock::now();
    // cout << "Model eval took " << std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()*1E-6 << " ms" << std::endl;
    // #endif

}


void HierarchicalRVmodel::remove_known_object()
{
    // double f, v, ti, Tp;
    // for (int j = 0; j < n_known_object; j++) {
    //     auto v = brandt::keplerian(data.t, KO_P[j], KO_K[j], KO_e[j], KO_w[j], KO_phi[j], data.M0_epoch);
    //     for (size_t i = 0; i < data.N(); i++) {
    //         mu[i] -= v[i];
    //     }
    // }
}

void HierarchicalRVmodel::add_known_object()
{
    // for (int j = 0; j < n_known_object; j++) {
    //     auto v = brandt::keplerian(data.t, KO_P[j], KO_K[j], KO_e[j], KO_w[j], KO_phi[j], data.M0_epoch);
    //     for (size_t i = 0; i < data.N(); i++) {
    //         mu[i] += v[i];
    //     }
    // }
}

int HierarchicalRVmodel::is_stable() const
{
    int stable_planets = 0;
    int stable_known_object = 0;

    for (size_t i = 0; i < data.Ns(); i++)
    {
        // Get the components
        const vector< vector<double> >& components = planets[i].get_components();
        if (components.size() == 0 && !known_object)
            return 0;
        
        if (components.size() != 0)
            stable_planets = AMD::AMD_stable(components, star_mass);

        if (known_object) {
            vector<vector<double>> ko_components;
            ko_components.resize(n_known_object);
            for (int j = 0; j < n_known_object; j++) {
                ko_components[j] = {KO_P[j], KO_K[j], KO_phi[j], KO_e[j], KO_w[j]};
            }
            
            stable_known_object = AMD::AMD_stable(ko_components, star_mass);
        }
    }

    return stable_planets + stable_known_object;
}


double HierarchicalRVmodel::perturb(RNG& rng)
{
    #if TIMING
    auto begin = std::chrono::high_resolution_clock::now();  // start timing
    #endif

    double logH = 0.;
    double tmid = 0.0;// data.get_t_middle();

    if(npmax > 0 && rng.rand() <= 0.75) // perturb planet parameters
    {
        for (auto &&p : planets)
        {
            logH += p.perturb(rng);
            p.consolidate_diff();
        }
        
        calculate_mu();
    }
    else if(rng.rand() <= 0.5) // perturb jitter(s) + known_object
    {
        if(data.datamulti)
        {
            for(int i=0; i<jitters.size(); i++)
                Jprior->perturb(jitters[i], rng);
        }
        else
        {
            Jprior->perturb(extra_sigma, rng);
        }

        if (studentt)
            nu_prior->perturb(nu, rng);


        if (known_object)
        {
            remove_known_object();

            for (int i=0; i<n_known_object; i++){
                KO_Pprior[i]->perturb(KO_P[i], rng);
                KO_Kprior[i]->perturb(KO_K[i], rng);
                KO_eprior[i]->perturb(KO_e[i], rng);
                KO_phiprior[i]->perturb(KO_phi[i], rng);
                KO_wprior[i]->perturb(KO_w[i], rng);
            }

            add_known_object();
        }
    
    }
    else
    {
        // for(size_t i=0; i<mu.size(); i++)
        // {
        //     mu[i] -= background;
        //     if(trend) {
        //         mu[i] -= slope * (data.t[i] - tmid) +
        //                     quadr * pow(data.t[i] - tmid, 2) +
        //                     cubic * pow(data.t[i] - tmid, 3);
        //     }
        //     if(data.datamulti) {
        //         for(size_t j=0; j<offsets.size(); j++){
        //             if (data.obsi[i] == j+1) { mu[i] -= offsets[j]; }
        //         }
        //     }
        // }

        // propose new vsys
        for (auto &&b : background)
        {
            Cprior->perturb(b, rng);
        }
        

        // propose new instrument offsets
        if (data.datamulti){
            for(unsigned j=0; j<offsets.size(); j++){
                individual_offset_prior[j]->perturb(offsets[j], rng);
            }
        }

        // propose new slope
        if(trend) {
            if (degree >= 1) slope_prior->perturb(slope, rng);
            if (degree >= 2) quadr_prior->perturb(quadr, rng);
            if (degree == 3) cubic_prior->perturb(cubic, rng);
        }

        // for(size_t i=0; i<mu.size(); i++)
        // {
        //     mu[i] += background;
        //     if(trend) {
        //         mu[i] += slope * (data.t[i] - tmid) +
        //                     quadr * pow(data.t[i] - tmid, 2) +
        //                     cubic * pow(data.t[i] - tmid, 3);
        //     }
        //     if(data.datamulti) {
        //         for(size_t j=0; j<offsets.size(); j++){
        //             if (data.obsi[i] == j+1) { mu[i] += offsets[j]; }
        //         }
        //     }
        // }

        calculate_mu();
    }


    #if TIMING
    auto end = std::chrono::high_resolution_clock::now();
    cout << "Perturb took ";
    cout << std::chrono::duration_cast<std::chrono::microseconds>(end-begin).count();
    cout << " μs" << std::endl;
    #endif

    return logH;
}

/// Calculate the log-likelihood for the current values of the parameters
double HierarchicalRVmodel::log_likelihood() const
{
    size_t N = data.N();
    auto sig = data.get_sigjoin();

    double logL = 0.;

    if (enforce_stability){
        int stable = is_stable();
        if (stable != 0)
            return -std::numeric_limits<double>::infinity();
    }


    #if TIMING
    auto begin = std::chrono::high_resolution_clock::now();  // start timing
    #endif

    if (studentt){
        return logL;
    //     // The following code calculates the log likelihood 
    //     // in the case of a t-Student model
    //     double var, jit;
    //     for(size_t i=0; i<N; i++)
    //     {
    //         if(data.datamulti)
    //         {
    //             jit = jitters[obsi[i]-1];
    //             var = sig[i]*sig[i] + jit*jit;
    //         }
    //         else
    //             var = sig[i]*sig[i] + extra_sigma*extra_sigma;

    //         logL += std::lgamma(0.5*(nu + 1.)) - std::lgamma(0.5*nu)
    //                 - 0.5*log(M_PI*nu) - 0.5*log(var)
    //                 - 0.5*(nu + 1.)*log(1. + pow(y[i] - mu[i], 2)/var/nu);
    //     }

    }

    else{
        double var, jit;
        for (size_t i = 0; i < N; i++)
        {
            // if(data.datamulti)
            // {
            //     jit = jitters[obsi[i]-1];
            //     var = sig[i]*sig[i] + jit*jit;
            // }
            // else
            var = sig[i] * sig[i] + extra_sigma * extra_sigma;

            logL += -halflog2pi - 0.5 * log(var) - 0.5 * (pow(data.yjoin[i] - mujoin[i], 2) / var);
        }
    }

    #if TIMING
    auto end = std::chrono::high_resolution_clock::now();
    cout << "Likelihood took " << std::chrono::duration_cast<std::chrono::nanoseconds>(end-begin).count()*1E-6 << " ms" << std::endl;
    #endif

    if(std::isnan(logL) || std::isinf(logL))
    {
        logL = std::numeric_limits<double>::infinity();
    }
    // cout << "logL: " << logL << endl;
    return logL;
}


void HierarchicalRVmodel::print(std::ostream& out) const
{
    // output precision
    out.setf(ios::fixed, ios::floatfield);
    out.precision(8);

    if (data.datamulti)
    {
        for(int j=0; j<jitters.size(); j++)
            out << jitters[j] << '\t';
    }
    else
        out << extra_sigma << '\t';

    if(trend)
    {
        out.precision(15);
        if (degree >= 1) out << slope << '\t';
        if (degree >= 2) out << quadr << '\t';
        if (degree == 3) out << cubic << '\t';
        out.precision(8);
    }
        
    if (data.datamulti){
        for (int j = 0; j < offsets.size(); j++)
        {
            out << offsets[j] << '\t';
        }
    }

    if(known_object){ // KO mode!
        for (auto P: KO_P) out << P << "\t";
        for (auto K: KO_K) out << K << "\t";
        for (auto phi: KO_phi) out << phi << "\t";
        for (auto e: KO_e) out << e << "\t";
        for (auto w: KO_w) out << w << "\t";
    }

    for (auto &&p : planets)
        p.print(out);

    out << staleness << '\t';

    if (studentt)
        out << nu << '\t';

    for (auto b : background)
        out << b << "\t";
}


string HierarchicalRVmodel::description() const
{
    string desc;
    string sep = "   ";

    if (data.datamulti)
    {
        for(int j=0; j<jitters.size(); j++)
           desc += "jitter" + std::to_string(j+1) + sep;
    }
    else
        desc += "extra_sigma" + sep;

    if(trend)
    {
        if (degree >= 1) desc += "slope" + sep;
        if (degree >= 2) desc += "quadr" + sep;
        if (degree == 3) desc += "cubic" + sep;
    }


    if (data.datamulti){
        for(unsigned j=0; j<offsets.size(); j++)
            desc += "offset" + std::to_string(j+1) + sep;
    }

    if(known_object) { // KO mode!
        for(int i=0; i<n_known_object; i++) 
            desc += "KO_P" + std::to_string(i) + sep;
        for(int i=0; i<n_known_object; i++) 
            desc += "KO_K" + std::to_string(i) + sep;
        for(int i=0; i<n_known_object; i++) 
            desc += "KO_phi" + std::to_string(i) + sep;
        for(int i=0; i<n_known_object; i++) 
            desc += "KO_ecc" + std::to_string(i) + sep;
        for(int i=0; i<n_known_object; i++) 
            desc += "KO_w" + std::to_string(i) + sep;
    }

    desc += "ndim" + sep + "maxNp" + sep;
    if(false) // hyperpriors
        desc += "muP" + sep + "wP" + sep + "muK";

    desc += "Np" + sep;

    if (npmax > 0) {
        for(int i = 0; i < npmax; i++) desc += "P" + std::to_string(i) + sep;
        for(int i = 0; i < npmax; i++) desc += "K" + std::to_string(i) + sep;
        for(int i = 0; i < npmax; i++) desc += "phi" + std::to_string(i) + sep;
        for(int i = 0; i < npmax; i++) desc += "ecc" + std::to_string(i) + sep;
        for(int i = 0; i < npmax; i++) desc += "w" + std::to_string(i) + sep;
    }

    desc += "staleness" + sep;
    if (studentt)
        desc += "nu" + sep;
    
    desc += "vsys";

    return desc;
}

/**
 * Save the options of the current model in a INI file.
 * 
*/
void HierarchicalRVmodel::save_setup() {
	std::fstream fout("kima_model_setup.txt", std::ios::out);
    fout << std::boolalpha;

    time_t rawtime;
    time (&rawtime);
    fout << ";" << ctime(&rawtime) << endl;

    fout << "[kima]" << endl;

    fout << "model: " << "HierarchicalRVmodel" << endl << endl;
    fout << "fix: " << fix << endl;
    fout << "npmax: " << npmax << endl << endl;

    fout << "hyperpriors: " << false << endl;
    fout << "trend: " << trend << endl;
    fout << "degree: " << degree << endl;
    fout << "multi_instrument: " << data.datamulti << endl;
    fout << "known_object: " << known_object << endl;
    fout << "n_known_object: " << n_known_object << endl;
    fout << "studentt: " << studentt << endl;
    fout << endl;

    fout << endl;

    fout << "[data]" << endl;
    fout << "Ns: " << data.Ns() << endl;
    fout << "N: " << data.N() << endl;
    fout << "file: " << data.datafile << endl;
    fout << "units: " << data.dataunits << endl;
    fout << "skip: " << data.dataskip << endl;
    fout << "multi: " << data.datamulti << endl;

    fout << "files: ";
    for (auto f: data.datafiles)
        fout << f << ",";
    fout << endl;

    fout.precision(15);
    fout << "M0_epoch: " << data.M0_epoch << endl;
    fout.precision(6);

    fout << endl;

    fout << "[priors.general]" << endl;
    fout << "Cprior: " << *Cprior << endl;
    fout << "Jprior: " << *Jprior << endl;
    if (trend){
        if (degree >= 1) fout << "slope_prior: " << *slope_prior << endl;
        if (degree >= 2) fout << "quadr_prior: " << *quadr_prior << endl;
        if (degree == 3) fout << "cubic_prior: " << *cubic_prior << endl;
    }
    if (data.datamulti)
        fout << "offsets_prior: " << *offsets_prior << endl;
    if (studentt)
        fout << "nu_prior: " << *nu_prior << endl;

    // if (planets.get_max_num_components()>0){
    //     auto conditional = planets.get_conditional_prior();

    //     if (false){
    //         fout << endl << "[prior.hyperpriors]" << endl;
    //         fout << "log_muP_prior: " << *conditional->log_muP_prior << endl;
    //         fout << "wP_prior: " << *conditional->wP_prior << endl;
    //         fout << "log_muK_prior: " << *conditional->log_muK_prior << endl;
    //     }

    //     fout << endl << "[priors.planets]" << endl;
    //     fout << "Pprior: " << *conditional->Pprior << endl;
    //     fout << "Kprior: " << *conditional->Kprior << endl;
    //     fout << "eprior: " << *conditional->eprior << endl;
    //     fout << "phiprior: " << *conditional->phiprior << endl;
    //     fout << "wprior: " << *conditional->wprior << endl;
    // }

    if (known_object) {
        fout << endl << "[priors.known_object]" << endl;
        for(int i=0; i<n_known_object; i++){
            fout << "Pprior_" << i << ": " << *KO_Pprior[i] << endl;
            fout << "Kprior_" << i << ": " << *KO_Kprior[i] << endl;
            fout << "eprior_" << i << ": " << *KO_eprior[i] << endl;
            fout << "phiprior_" << i << ": " << *KO_phiprior[i] << endl;
            fout << "wprior_" << i << ": " << *KO_wprior[i] << endl;
        }
    }

    fout << endl;
	fout.close();
}

