#!/usr/bin/env python

"""
Example of the KS test.
"""

import matplotlib.pyplot as pl
from scipy.stats import norm, kstest
import numpy as np

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

N = 30 # number of samples

# a random sample drawn from a normal distribution N(0,1)
x = np.random.randn(N)

xs = np.linspace(-4, 4, 1000)

# get cumulative distribution
[xn, bins] = np.histogram(x, bins=xs)
xn = xn/float(N)
cs = np.cumsum(xn)

binmids = bins[0:-1] + (bins[1]-bins[0])/2.

ncdf = norm.cdf(binmids, 0., 1.)

imax = np.argmax(np.abs(ncdf-cs))

# test data against normal distribution
#D, pv = kstest(x, 'norm')
D, pv = kstest(x, lambda x: norm.cdf(x, 0., 1.))

#pl.hist(x, bins=binmids, 'b', normed=True, cumulative=True, histtype='step', label='$S_n(x)$')
pl.step(bins[0:-1], cs, 'b', label='$S_n(x)$')
pl.plot(binmids, ncdf, 'r', label='$P(x)$')
pl.plot([binmids[imax], binmids[imax]], [ncdf[imax], cs[imax]], 'k--', label='$D_n = %.2f$' % D)

pl.grid(True)
pl.legend(loc='upper left')
ax = pl.gca()
ax.set_xlabel('$x$')
ax.set_ylabel('$P(x)$')

ax.text(-0.5, 0.1, '$D_n = \\textrm{max}|P(x)-S_n(x)|$' % D, fontsize=16)

fig.subplots_adjust(bottom=0.12)

pl.show()
fig.savefig('../kstest.pdf')