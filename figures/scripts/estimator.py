#!/usr/bin/env python

"""
Make plots of the Gaussian/normal distribution for different standard devaitions
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
import numpy as np

theta0 = 1.5
mus = [1.5, 3.] # the mean, mu
sigmas = [1.2, 0.15] # standard deviations, sigma
markers = ['b-', 'r-']

thetas = np.linspace(-5, 5, 1000) # x

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(4,5), dpi=100)

# plot pdfs
for i, sigma in enumerate(sigmas):
  pl.plot(thetas, norm.pdf(thetas, mus[i], sigma), markers[i], label='$\hat{\\theta}_%d$' % (i+1))

ax = pl.gca()
ax.set_xlabel('$\hat{\\theta}$', fontsize=14)
ax.set_ylabel('$p(\hat{\\theta}|\\theta,I)$', fontsize=14)
ax.set_xticks((theta0,))
ax.set_xticklabels(('$\\theta$',))

ax.legend(loc='upper left', frameon=False)

fig.subplots_adjust(bottom=0.15, left=0.18)

pl.savefig('../estimator.pdf')
pl.show()

