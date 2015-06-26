#!/usr/bin/env python

"""
Make plots of the Poisson distribution for different rates
"""

import matplotlib.pyplot as pl
from scipy.stats import poisson

mus = [0.5, 1., 3., 5.] # rates, mu
markers = ['bo-', 'ro-', 'mo-', 'ko-']

x = range(0, 11) # number of counts, r

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

# plot pdfs
for i, mu in enumerate(mus):
  pl.plot(x, poisson.pmf(x, mu), markers[i], label='$\mu=%.1f$'%mu)

ax = pl.gca()
ax.set_xlabel('Number of counts, $r$', fontsize=14)
ax.set_ylabel('$p(r)$', fontsize=14)
ax.text(2, 0.55, '$p(r) = \\frac{\mu^r e^{-\mu}}{r!}$', fontsize=26, bbox={'facecolor': 'none', 'pad':20, 'ec': 'r'})

ax.legend(loc='best', frameon=False)

fig.subplots_adjust(bottom=0.15)

pl.savefig('../poisson.pdf')
pl.show()

