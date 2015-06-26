#!/usr/bin/env python

"""
Show how the posterior gets updated as a set of coin tosses are generated for a biased coin.
Assume a flat prior on the bias weighting and also a Gaussian prior.
"""

import matplotlib.pyplot as pl
from scipy.stats import norm, kstest
import numpy as np

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(12,10), dpi=100)

# numbers of coin tosses
nt = [0, 1, 2, 5, 10, 50, 100, 500, 1000]

bias = 0.3 # biased towards tails

# bias values
H = np.linspace(0., 1., 1000)

# priors
priorflat = np.ones(len(H))
sigmah = 0.05
muh = 0.5
priorgauss = (1./np.sqrt(2.*np.pi*sigmah**2))*np.exp(-0.5*(H-muh)**2/sigmah**2)

curheads = 0. # current number of heads
for i, n in enumerate(nt):
  # generate coin tosses (making sure to include previous ones)
  if n > 0:
    rc = np.random.rand(n-nprev)
    curheads = curheads + len(np.zeros(n-nprev)[rc<bias])
  
  # compute likelihood
  L = H**curheads * (1.-H)**(n-curheads)
  
  # compute posterior
  post1 = L*priorflat
  post2 = L*priorgauss
  
  # normalise posterior
  post1 = post1/np.trapz(post1, H)
  post2 = post2/np.trapz(post2, H)
  
  # plot posterior
  pl.subplot(3,3,i+1)
  pl.plot(H, post1, 'b', label='$p(H|d,I)$ Uniform prior')
  pl.plot(H, post2, 'r', label='$p(H|d,I)$ Gaussian prior')
  pl.plot(H, priorgauss, 'k--', label='$p(H|I)$ Gaussian')
  ax = pl.gca()
  ax.set_yticklabels([])
  ax.set_yticks([])
  
  if i == 0:
    pl.legend(loc='lower left', fancybox=True, framealpha=0.3, prop={'size': 12})
  
  if i % 3 == 0:
    ax.set_ylabel('$p(H|d,I)$')
    
  if i > 5:
    ax.set_xlabel('$H$')
  else:
    ax.set_xticklabels([])
 
  ax.text(0.65, 0.8*ax.get_ylim()[1], '$n=%d$' % n, fontsize=16)
 
  nprev = n

pl.tight_layout()
#fig.subplots_adjust(bottom=0.12)

pl.show()
fig.savefig('../coin_toss_2.pdf')