#!/usr/bin/env python

"""
Make plots of the Student's t-distribution for different degrees of freedom
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
from scipy.stats import t
import numpy as np

mu = 0. # the mean, mu
nus = [1., 2., 5, 10, 100] # standard deviations, sigma
markers = ['b-', 'r-', 'm-', 'c-', 'g-']

x = np.linspace(-6, 6, 1000) # x

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

# plot pdfs
for i, nu in enumerate(nus):
  pl.plot(x, t.pdf(x, nu), markers[i], label='$\\nu=%d$'%nu)

# plot a Gaussian for comparison
pl.plot(x, norm.pdf(x, mu, 1.), 'k--', label='$N(0,1)$')

ax = pl.gca()
ax.set_xlabel('$t$', fontsize=14)
ax.set_ylabel('$p(t)$', fontsize=14)

ax.legend(loc='best', frameon=False)

fig.subplots_adjust(bottom=0.15)

pl.savefig('../studentst.pdf')
pl.show()

