#!/usr/bin/env python

"""
Make plots showing how to calculate the p-value
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
from scipy.special import erf
import numpy as np

mu = 0. # the mean, mu
sigma = 1. # standard deviation

x = np.linspace(-4, 4, 1000) # x

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(7,4), dpi=100)

# value of x for calculating p-value
Z = 1.233

y = norm.pdf(x, mu, sigma)

# plot pdfs
pl.plot(x, y, 'r')
pl.plot([-Z, -Z], [0., np.max(y)], 'k--')
pl.plot([Z, Z], [0., np.max(y)], 'k--')

pl.fill_between(x, np.zeros(len(x)), y, where=x<=-Z, facecolor='green', interpolate=True, alpha=0.6)
pl.fill_between(x, np.zeros(len(x)), y, where=x>=Z, facecolor='green', interpolate=True, alpha=0.6)

pvalue = 1.-erf(Z/np.sqrt(2.))

ax = pl.gca()
ax.set_xlabel('$Z$', fontsize=14)
ax.set_ylabel('$p(Z)$', fontsize=14)
ax.set_xlim(-4, 4)
ax.grid(True)

ax.text(Z+0.1, 0.3, '$Z_{\\textrm{obs}} = 1.233$', fontsize=16)
ax.text(-3.6, 0.31, '$p$-value$= %.2f$' % pvalue, fontsize=18,
        bbox={'facecolor': 'none', 'pad':12, 'ec': 'r'})

fig.subplots_adjust(bottom=0.15)

pl.savefig('../pvalue.pdf')
pl.show()

