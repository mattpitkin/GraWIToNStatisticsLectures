#!/usr/bin/env python

"""
Make plots of the Gaussian/normal distribution for different standard devaitions
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
import numpy as np

mu = 5. # the mean, mu
sigmas = [0.5, 1., 2.] # standard deviations, sigma
markers = ['b-', 'r-', 'k-']

x = np.linspace(0, 10, 1000) # x

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

# plot pdfs
for i, sigma in enumerate(sigmas):
  pl.plot(x, norm.pdf(x, mu, sigma), markers[i], label='$\sigma=%.1f$'%sigma)

ax = pl.gca()
ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$p(x)$', fontsize=14)
ax.text(1, 0.65, '$\mu = 5$', fontsize=22, bbox={'facecolor': 'none', 'pad':20, 'ec': 'r'})

ax.legend(loc='best', frameon=False)

fig.subplots_adjust(bottom=0.15)

pl.savefig('../gaussian.pdf')
pl.show()

