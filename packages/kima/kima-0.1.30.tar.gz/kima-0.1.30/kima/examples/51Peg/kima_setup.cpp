#include "kima.h"

RVmodel::RVmodel():fix(false),npmax(1)
{
    // priors for the systemic velocity and jitter
    Cprior = make_prior<Uniform>(-10., 10.); // m/s
    Jprior = make_prior<ModifiedLogUniform>(1., 1000.); // m/s

    // conditional priors for the planetary parameters
    auto conditional = planets.get_conditional_prior();
    conditional->Pprior = make_prior<LogUniform>(0.2, 2000.); // days
    conditional->Kprior = make_prior<ModifiedLogUniform>(1., 1000.); // m/s
    conditional->eprior = make_prior<Uniform>(0., 1.);
    conditional->phiprior = make_prior<Uniform>(0., 2*PI);
    conditional->wprior = make_prior<Uniform>(0., 2*PI);
}


int main(int argc, char** argv)
{
    datafile = "51Peg.rv";
    load(datafile, "ms", 0);

    Sampler<RVmodel> sampler = setup<RVmodel>(argc, argv);
    sampler.run(500);

    return 0;
}
