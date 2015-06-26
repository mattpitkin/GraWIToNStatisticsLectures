#!/usr/bin/env python

"""
Make plots of the cumulative distribution functions for Gaussian/normal and uniform distributions  
standard devaitions
"""

import matplotlib.pyplot as pl
from scipy.stats import norm, uniform
import numpy as np

# normal distribution
mu = 0. # the mean, mu
sigma = 1 # standard deviations, sigma

x = np.linspace(-4, 4, 1000) # x

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

# plot pdfs
pl.plot(x, norm.cdf(x, mu, sigma), 'b--', label='Gaussian')
pl.plot(x, uniform.cdf(x, -1, 2.), 'r', label='Uniform')

ax = pl.gca()
ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('CDF, $P(x)$', fontsize=14)
ax.text(1, 0.2, '$\mu = 0,~\sigma=1$', color='blue', fontsize=18)
ax.text(1, 0.1, '$a = -1,~b=1$', color='red', fontsize=18)

ax.legend(loc='upper left', frameon=False)

fig.subplots_adjust(bottom=0.15)

pl.savefig('../ch.pdf')
pl.show()

