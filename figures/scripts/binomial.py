#!/usr/bin/env python

"""
Make plots of the Binomial distribution for different outcome probabilities
"""

import matplotlib.pyplot as pl
from scipy.stats import binom

theta = 0.5 # probability of success theta
Ns = [1, 5, 10, 15] # number of trials
markers = ['bo-', 'ro-', 'mo-', 'ko-']

x = range(0, 21) # number of successes, r

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

# plot pdfs
for i, N in enumerate(Ns):
  pl.plot(x, binom.pmf(x, N, theta), markers[i], label='$N=%d$'%N)

ax = pl.gca()
ax.set_xlabel('Number of successes, $r$', fontsize=14)
ax.set_ylabel('$p_N(r)$', fontsize=14)
ax.text(4, 0.4, '$p_N(r) = \\frac{N!}{r!(N-r)!}\\theta^r(1-\\theta)^{N-r}$', fontsize=22, bbox={'facecolor': 'none', 'pad':20, 'ec': 'r'})

ax.legend(loc='lower right', frameon=False)

fig.subplots_adjust(bottom=0.15)

pl.savefig('../binomial.pdf')
pl.show()

