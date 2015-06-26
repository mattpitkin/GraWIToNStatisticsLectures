#!/usr/bin/env python

"""
An MCMC example - sample a lopsided Gaussian posterior
"""

import matplotlib.pyplot as pl
import numpy as np
from scipy.stats import norm
import matplotlib.gridspec as gridspec
import sys

# define the posterior
def posterior(x):
  return 0.75*norm.pdf(x, -0.75, 0.75) + 1.*norm.pdf(x, 0.75, 0.75)

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)

# x values
x = np.linspace(-4, 4, 1000)

# show posterior (for plotting)
y = posterior(x)
normconst = np.trapz(y, x)
y = y/normconst

# number of samples
N = 50000

# samples to output plots at
ns = [5, 99, 199, 499, 999, 9999, 49999]

# initial sample of x
xs = [2.]

# get posterior at current sample
xcur = xs[0]
curpost = posterior(xs[0])

# proposal distribution
sigmaprop = 0.5

# number of points in posterior sample histogram
nhist = 20

firstaccept = 0

count = 0

# perform MCMC
for i in range(1, N+1):
  # generate new sample using the proposal
  xnew = xs[i-1] + sigmaprop*np.random.randn()

  # get posterior value at new sample
  newpost = posterior(xnew)

  # get Metropolis-Hastings ratio
  ratio = newpost/curpost

  # accept new point
  randval = np.random.rand(1)
  if ratio > randval and xnew <= x[-1] and xnew >= x[0]:
    xs.append(xnew)
    if firstaccept == 0:
      firstaccept = 1
  else: # reject new point
    xs.append(xs[i-1])

  # produce plot
  if i in ns or firstaccept == 1:
    fig = pl.figure(figsize=(10,5), dpi=100)
    gs = gridspec.GridSpec(1, 2, width_ratios=[2.5,1])

    pl.subplot(gs[0])

    # plot posterior
    pl.plot(x, y, 'k--', label='Posterior')

    # plot proposal distribution
    q1 = 0.25*norm.pdf(x, xs[i-1], sigmaprop)
    q2 = 0.25*norm.pdf(x, xnew, sigmaprop)
    pl.plot(x, q1, 'b')
    pl.plot(x, q2, 'b--')

    pl.plot(xs[i-1], curpost/normconst, 'bo', label='$p(x_1|I)$')
    pl.plot(xnew, newpost/normconst, 'bv', label='$p(x_2|I)$')

    # get the q values
    pl.plot(xcur, 0.25*norm.pdf(xcur, xnew, sigmaprop), 'ro', label='$q(x_1|x_2,I)$')
    pl.plot(xnew, 0.25*norm.pdf(xnew, xs[i-1], sigmaprop), 'rv', label='$q(x_2|x_1,I)$')

    pl.plot([xcur, xcur], [0., curpost/normconst], 'g--')
    pl.plot([xnew, xnew], [0., newpost/normconst], 'g--')

    ax = pl.gca()
    # plot arrow between points
    if xnew-xcur > 0:
      hl = -1.
    else:
      hl = 1.
    
    ax.arrow(xcur, curpost/normconst, xnew-xcur+hl*0.07, 0., head_width=0.006, head_length=0.07, fc='k', ec='k')

    ax.set_yticklabels([])
    ax.set_xlabel('$x$')

    pl.legend(loc='upper left', numpoints=1, fancybox=True, framealpha=0.3, prop={'size': 14})

    # plot histogram of samples
    if i > 5:
      nh, bins, patches = pl.hist(xs, bins=nhist, histtype='stepfilled', normed=True)
      pl.setp(patches, 'facecolor', 'b', 'alpha', 0.1)
    
    ax.text(2.5, 0.9*ax.get_ylim()[1], '$n = %d$' % (i+1), fontsize=15)

    # plot samples
    pl.subplot(gs[1])

    pl.plot(range(1,i+2), xs, 'b.')
    ax = pl.gca()
    ax.set_xlim(0, i+2)
    ax.set_ylim(np.min(xs)-0.1, np.max(xs)+0.1)
    ax.set_ylabel('$x$')
    if i > 1000:
      pl.xticks(rotation=45)
    
    pl.tight_layout()

    pl.show()

    count = count+1
    fig.savefig('../mcmc_example_%d.pdf' % count)

    fig.clf()
    pl.close(fig)

    firstaccept = np.inf

  # update indices (do this here so the plots work) 
  if ratio > randval and xnew <= x[-1] and xnew >= x[0]:
    curpost = newpost
    xcur = xnew

