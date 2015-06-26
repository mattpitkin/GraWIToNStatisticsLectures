#!/usr/bin/env python

"""
Show how well the Gaussian approximation does for different pdfs - use bimodal normal distribution
seperated by different amounts
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
import numpy as np

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)

heights = [0.7, 1.]

# means of Gaussians
mus = [[0., 0.], [-0.4, 0.4], [-1., 1.]] 
sigma = 0.4

x = np.linspace(-4, 4, 5000) # x

fig = pl.figure(figsize=(10,5), dpi=100)

for i in range(3):
  pl.subplot(1,3,i+1)
  
  # create distribution
  y1 = norm.pdf(x, mus[i][0], sigma)
  y2 = norm.pdf(x, mus[i][1], sigma)
 
  y = heights[0]*y1 + heights[1]*y2
  y = y/np.trapz(y, x) # normalise
  
  pl.plot(x, y, 'b', label='pdf')
 
  # find maximum posterior
  imax = np.argmax(y)
  mumax = x[imax]
  
  # get second derivative of function log of function
  dx = x[1]-x[0]
  dy = np.gradient(np.log(y), dx)
  ddy = np.gradient(dy, dx)
 
  # sigma from second derivative  
  sigmamax = np.sqrt(1./(-ddy[imax]))
  
  ygauss = norm.pdf(x, mumax, sigmamax)
 
  pl.plot(x, ygauss, 'k--', label='Gaussian approx.')
 
  if i==2:
    pl.legend(loc='upper left', fancybox=True, framealpha=0.3, prop={'size': 14})
 
  ax = pl.gca()
  ax.text(-3.5, 0.05, '%d)' % (i+1), fontsize=16)
  ax.set_xticklabels([])
  ax.set_yticklabels([])
  ax.set_xlim(x[0], x[-1])

pl.tight_layout()

pl.savefig('../gaussian_approximation.pdf')
pl.show()
  
fig.clf()
pl.close(fig)

