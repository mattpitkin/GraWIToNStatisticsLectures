#!/usr/bin/env python

"""
Make plots of the distributions of a simple hypothesis test statistic, but with very disjoint distributions
for the test statistic.
The two hypotheses are:
 H_0 = x is drawn from N(-2, 1)
 H_1 = x is drawn from N(4, 1)
and the test statistic t is t=x
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
import numpy as np

mu = [-2., 6.] # the mean, mu
sigma = 1.
markers = ['b-', 'r-', 'k-']

x = np.linspace(-6., 10., 1500) # x

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(7,5), dpi=100)

t1 = norm.pdf(x, mu[0], sigma)
t2 = norm.pdf(x, mu[1], sigma)

c1 = norm.cdf(x, mu[0], sigma)
c2 = norm.cdf(x, mu[1], sigma)

tcrit = 2.

pI = 1.-c1[x<=tcrit][-1] # probability of type I error
pII = c2[x>=tcrit][0]

# plot pdfs of the test statistic under both hypotheses
pl.plot(x, t1, 'b', label='$H_0$')
pl.plot(x, t2, 'r', label='$H_1$')
pl.plot([tcrit, tcrit], [0., np.max(t1)], 'k--')

pl.fill_between(x, np.zeros(len(x)), t1, where=x>=tcrit, alpha=0.6, facecolor='green', interpolate=True)
pl.fill_between(x, np.zeros(len(x)), t2, where=x<tcrit, alpha=0.6, facecolor='cyan', interpolate=True)

ax = pl.gca()
ax.set_xlabel('$t$', fontsize=14)
ax.set_ylabel('$p(t)$', fontsize=14)
ax.set_xlim(x[0], x[-1])
ax.text(3.+tcrit, 0.35, '$P(I) = %.5f$' % pI, fontsize=16)
ax.text(3.+tcrit, 0.31, '$P(II) = %.5f$' % pII, fontsize=16)
ax.text(-0.8+tcrit, 0.27, 'Acceptance region', fontsize=16, rotation=90) 
ax.text(0.3+tcrit, 0.25, 'Critical region', fontsize=16, rotation=270) 

ax.legend(loc='upper left', frameon=False)

fig.subplots_adjust(bottom=0.15)

pl.savefig('../hypothesis_test_2.pdf')
pl.show()

