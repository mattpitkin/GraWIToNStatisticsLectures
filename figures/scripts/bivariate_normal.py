#!/usr/bin/env python

"""
Make plots of the bivariate normal distribution
"""

import matplotlib.pyplot as pl
from scipy.stats import multivariate_normal
import numpy as np

mus = [0., 0] # the mean, mu
corcoeffs = [-0.9, -0.3, 0., 0.3, 0.9]
sigmas = [1., 1.]

x, y = np.mgrid[-4:4:.01, -8:8:.01]
pos = np.empty(x.shape + (2,))
pos[:, :, 0] = x
pos[:, :, 1] = y

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(10,5), dpi=100)

# plot pdfs
for i, coeffs in enumerate(corcoeffs):
  pl.subplot(1,5,i+1)
  rv = multivariate_normal(mus, [[sigmas[0], sigmas[0]*sigmas[1]*coeffs], [sigmas[0]*sigmas[1]*coeffs, sigmas[1]]])
  pl.contour(x, y, rv.pdf(pos))
  pl.grid(True)
  ax = pl.gca()
  ax.set_xticks((-3,0,3))
  ax.set_yticks((-3,0,3))
  ax.set_xticklabels(('-3','0','3'))
  ax.set_yticklabels(('-3','0','3'))
  ax.set_xlabel('$x$', fontsize=14)
  if i == 0:
    ax.set_ylabel('$y$', fontsize=14)
  ax.text(-1.5, 5.7, '$\\rho = %.1f$' % coeffs, fontsize=16)

fig.subplots_adjust(bottom=0.25)

pl.savefig('../bivariate_normal.pdf')
pl.show()

