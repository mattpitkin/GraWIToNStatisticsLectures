#!/usr/bin/env python

"""
Make plots of the chi-squared distribution for different degrees of freedom
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
from scipy.stats import chi2
import numpy as np

mu = 0. # the mean, mu
nus = [1., 3, 5., 10., 15.] # standard deviations, sigma
markers = ['b-', 'r-', 'm-', 'c-', 'g-']

x = np.linspace(0, 25, 1000) # x

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

# plot pdfs
for i, nu in enumerate(nus):
  pl.plot(x, chi2.pdf(x, nu), markers[i], label='$\\nu=%d$'%nu)

# plot a Gaussian for comparison
pl.plot(x, norm.pdf(x, nus[-1], np.sqrt(2.*nus[-1])), 'k--',
        label='$N(%d,%.1f)$' % (nus[-1], np.sqrt(2.*nus[-1])))

ax = pl.gca()
ax.set_xlabel('$\chi^2$', fontsize=14)
ax.set_ylabel('$p(\chi^2)$', fontsize=14)
ax.set_ylim(0., 1.)

ax.legend(loc='best', frameon=False)

fig.subplots_adjust(bottom=0.15)

pl.savefig('../chisquared.pdf')
pl.show()

