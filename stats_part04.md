latex input:	mmd-beamer-header-11pt
Title:		Part 4: Practical Bayesian methods
Date:		25 March 2015
Author:		Matthew Pitkin
Affiliation:	University of Glasgow
LaTeX xslt:	beamer
latex mode:	beamer
Theme:		m
Event:		GraWIToN School
latex input:	mmd-beamer-begin-doc
latex footer:	mmd-beamer-footer

<!--
% Part 4 of my lecture course on statistics for the GraWIToN school
%
% Practical Bayesian methods
-->


### Overview ###

In this part of the course we will discuss a practical method for Bayesian parameter estimation:

* Markov chain Monte Carlo (MCMC)

This method is now very commonly used to perform parameter estimation for multi-dimensional
posterior parameter spaces.



### Markov chain Monte Carlo (MCMC) ###

**Markov chain Monte Carlo** (MCMC)

* Markov chain - a sequence of random variables where the probability of a subsequent state only depends
on the current state (they are "memoryless")
* Monte Carlo - an algorithm relying on repeated random sampling

So, a MCMC is a class of algorithms for drawing random samples that have a Markovian property.

We are particularly interesting in the **Metropolis-Hastings algorithm**. This can be used to efficiently
draw samples from an underlying probability distribution.



### MCMC demonstration ###

The Metropolis-Hastings algorithm (simplified to a 1D case):

* choose some initial random point in the parameter space, $x_1$, and calculate posterior $p(x_1|d,I)$
* centre a new pdf $q(x'|x_1,I)$, the **proposal distribution**, at $x_1$
* randomly draw a point from $x_2 \sim q(x'|x_1,I)$, and calculate posterior $p(x_2|d,I)$

Now compute the ratio
\\[
R = \frac{p(x_2|d,I)}{p(x_1|d,I)} \frac{q(x_2|x_1,I)}{q(x_1|x_2,I)}
\\]



### MCMC demonstration ###

The Metropolis-Hastings algorithm:

* accept the point $x_2$ if $R > 1$ (go uphill in posterior)
* if $R<1$
    * accept the point $x_2$ with a probability $R$ (go downhill in posterior)
    * otherwise reject the new point $x_2$ and set $x_2 = x_1$

This process gets repeated many times to build up a chain of samples.

Note: in general the proposal distribution will be Gaussian, so will be symmetric and
$\frac{q(x_2|x_1,I)}{q(x_1|x_2,I)} = 1$. This ratio is required to maintain **detailed balance**,
i.e. there should be the same probability to go forward along the chain as to run it in reverse.



### MCMC demonstration ###

![][mcmc_example_1]

[mcmc_example_1]: figures/mcmc_example_1.pdf "MCMC example" height="250px"



### MCMC demonstration ###

So the Metropolis Algorithm generally (but not always) moves uphill, towards the peak
of the posterior pdf.

_Remarkable facts_:

* The sequence of points $\{x_1, x_2, \ldots, x_n\}$ represent samples from the marginalised
posterior $p(x|d,I)$
* We can make a histogram of $\{x_1, x_2, \ldots, x_n\}$ and use it to compute the mean and variance
of $x$



### MCMC demonstration ###

![][mcmc_example_1]



### MCMC demonstration ###

![][mcmc_example_2]

[mcmc_example_2]: figures/mcmc_example_2.pdf "MCMC example" height="250px"



### MCMC demonstration ###

![][mcmc_example_3]

[mcmc_example_3]: figures/mcmc_example_3.pdf "MCMC example" height="250px"



### MCMC demonstration ###

![][mcmc_example_4]

[mcmc_example_4]: figures/mcmc_example_4.pdf "MCMC example" height="250px"



### MCMC demonstration ###

![][mcmc_example_5]

[mcmc_example_5]: figures/mcmc_example_5.pdf "MCMC example" height="250px"



### MCMC demonstration ###

![][mcmc_example_6]

[mcmc_example_6]: figures/mcmc_example_6.pdf "MCMC example" height="250px"



### MCMC demonstration ###

![][mcmc_example_7]

[mcmc_example_7]: figures/mcmc_example_7.pdf "MCMC example" height="250px"



### MCMC demonstration ###

![][mcmc_example_8]

[mcmc_example_8]: figures/mcmc_example_8.pdf "MCMC example" height="250px"



### MCMC tuning ###

If we don't choose a start point close to the bulk of the posterior it may take time
for the chain to converge on that area, so (given a non-infinite amount of samples)
a number of initial points may need to be _discarded_ during the **burn-in**.

(A couple of) diagnostic <!--\href{http://support.sas.com/documentation/cdl/en/statug/63347/HTML/default/viewer.htm\#statug\_introbayes\_sect008.htm}{methods}--> to assess convergence are:

* Geweke's test - test whether the means of an early part of the chain are consistent with the means for a later part
* Gelman-Rubin test - test whether the variances of two parallel chains are consistent

Although just checking by eyeball is often a good way to proceed.



### MCMC tuning ###


MCMC chains are not necessarily uncorrelated (not entirely Markovian!), so you can
calculate the autocorrelation length of the chains and thin them accordingly. This
can also be used as a test of convergence, in that the autocorrelation length may be large
during the burn in phase.



### MCMC tuning ###

If you have an infinite chain (almost) any choice of start position and proposal would
produce the marginalised posterior, but we can only practically produce a finite number
of samples, e.g. $100\,000\text{s}$ or $1\,000\,000\text{s}$

For efficient sampling we could have:

* a proposal that quite closely matches the posterior being sampled (e.g. via adjusting the proposal during **burn-in** based on covariance of currently collected samples)
* use a parameterisation where the parameters are (close to) independent
* simulated annealing (flattening the likelihood by "raising the temperature" during a **burn-in** period)



### MCMC tuning ###

Simple MCMC methods can have problems when:

* posterior is very tightly constrained within a very small part of the allowed parameter space
* posterior is multi-modal
* posterior has oddly shaped degeneracies between parameters

(A couple of) methods to address these are e.g.

* parallel tempering
* ensemble samplers



### Further advanced methods ###

There are lots of other advanced methods suitable for dealing with more complex situations, e.g.:

* <!--\href{http://en.wikipedia.org/wiki/Nested_sampling_algorithm}{Nested sampling}--> (evaluate _evidence_ integrals)
* <!--\href{http://en.wikipedia.org/wiki/Principal_component_analysis}{Principle component analysis (PCA) (data compression)}-->
* <!--\href{http://en.wikipedia.org/wiki/Reversible-jump_Markov_chain_Monte_Carlo}{Reversible Jump MCMC}-->
* <!--\href{http://en.wikipedia.org/wiki/Bayesian_hierarchical_modeling}{Hierarchical models}-->
* <!--\href{http://en.wikipedia.org/wiki/Approximate_Bayesian_computation}{Approximate Bayesian Computation} (ABC)-->
* Non-parameteric methods
    * <!--\href{http://en.wikipedia.org/wiki/Kriging}{Gaussian processes}-->
    * <!--\href{http://en.wikipedia.org/wiki/Dirichlet_process}{Dirichlet processes}-->
* <!--\href{http://en.wikipedia.org/wiki/Bayesian_network}{Bayesian neural networks}-->

It is a large and rapidly evolving field!
