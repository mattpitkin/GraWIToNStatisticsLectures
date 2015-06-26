#!/usr/bin/env python

"""
Make plots demonstrating the central limit theorem using values drawn from an exponential distribution
"""

import matplotlib.pyplot as pl
import numpy as np
from scipy.stats import expon
from scipy.stats import norm

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(7,5), dpi=150)

Ns = [5, 10, 100] # number of samples for the distribution
scale = 1.

samples=10000

# variance of exponential distributions
x = np.linspace(expon.ppf(0.01), expon.ppf(0.995), 200)
rv = expon()

pl.subplot(2,2,1)
pl.plot(x, rv.pdf(x), 'k-')
ax = pl.gca()
ax.set_xlabel('$x$', fontsize=14)
ax.set_ylabel('$p(x)$', fontsize=14)
ax.set_title('Exponential Distribution', fontsize=14)
ax.text(2, 0.8, '$\mu = 1, \sigma^2 = 1$', fontsize=16)

x2 = np.linspace(0., scale+3.*np.sqrt(rv.var()), 100)

# draw n samples from an exponential distributions 10000 times
for i, n in enumerate(Ns):
  samps = np.random.exponential(scale, (n, samples))
  samplemeans = np.mean(samps, axis=0) 

  pl.subplot(2,2,i+2)
  pl.hist(samplemeans, bins=25, normed=True, histtype='step', label='n=%d'%n)
  pl.plot(x2, norm.pdf(x2, scale, np.sqrt(rv.var()/n)), 'm--')
  pl.plot([scale, scale], [0., 1./np.sqrt(np.pi*2.*rv.var()/n)+0.2], 'k--')
  ax = pl.gca()
  ax.text(2.5, 0.8*ax.get_ylim()[1], '$n=%d$'%n)
  ax.set_ylabel('$p(\hat{\mu}_x|I)$', fontsize=14)
  ax.set_xlabel('$\hat{\mu}_x$', fontsize=14)
  ax.set_xticks((0.,1.,2.,3.,4.))

fig.subplots_adjust(hspace=0.3, wspace=0.28, bottom=0.12)

pl.savefig('../central_limit_theorem.pdf')
pl.show()

