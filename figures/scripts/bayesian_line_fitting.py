#!/usr/bin/env python

"""
Produce the posterior on the parameters of a line (assuming uniform priors) and plot this with the
marginal likelihood for each parameter
"""

import matplotlib.pyplot as pl
import numpy as np

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)

# x values
x = np.linspace(-5, 5, 6)

# gradient
m = 0.75

# y intercept
c = 1.

# line
y = m*x + c

# noise with sigma = 1
sigma = 1.;
n = np.random.randn(len(x))

d = y + n # the x "data"

# get the least squares fit values for m and c
mfit, cfit = np.linalg.lstsq(np.vstack([x, np.ones(len(x))]).T, d)[0]
yfit = mfit*x + cfit

fig = pl.figure(figsize=(12,10), dpi=100)

pl.subplot(2,2,2) # plot the data in the upper right corner

# plot data points line + noise
pl.plot(x, d, 'bx', markersize=10, mew=1, label='$x$ data')
pl.plot(x, y, 'k-', label='True line')
pl.plot(x, yfit, 'r-', label='Best fit line')

pl.grid(True)
pl.legend(loc='upper left')
ax = pl.gca()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

# m and c grid
ms = np.linspace(-3., 3., 200)
cs = np.linspace(-3., 3., 200)

logpost = np.zeros((200,200))

for i in range(200):
  for j in range(200):
    logpost[i,j] = -np.sum(0.5*(d-(ms[i]*x + cs[j]))**2/sigma**2)

# convert log posterior into posterior
post = np.exp(logpost-np.max(logpost))

pl.subplot(2,2,3)
pl.contour(ms, cs, post)
pl.plot(m, c, 'kx', markersize=10, mew=1, label='True value')
pl.legend(loc='lower left')
pl.grid(True)
ax = pl.gca()
ax.set_xlabel('$m$')
ax.set_ylabel('$c$')

# marginalise over c
postm = np.apply_along_axis(np.trapz, 1, post, cs)
postm = postm/np.trapz(postm, ms) # normalise

# marginalise over m
postc = np.apply_along_axis(np.trapz, 0, post, ms)
postc = postc/np.trapz(postc, cs) # normalise

# get maximum posterior position
mi = np.argmax(postm)
ci = np.argmax(postc)

pl.subplot(2,2,1)
pl.plot(ms, postm, 'b')
pl.plot([m, m], [0, np.max(postm)], 'k--', label='True value')
pl.plot(ms[mi], np.max(postm), 'o', markersize=10)
pl.legend(loc='lower left')
ax = pl.gca()
ax.set_xlabel('$m$')
ax.set_ylabel('$p(m|d,I)$')
ax.text(-2.8, 0.9*np.max(postm), 'max. posterior $m = %.2f$' % ms[mi], fontsize=16)
ax.text(-2.8, 0.8*np.max(postm), 'max. likelihood $\hat{m} = %.2f$' % mfit, fontsize=16)

pl.subplot(2,2,4)
pl.plot(cs, postc, 'b')
pl.plot([c, c], [0, np.max(postc)], 'k--', label='True value')
pl.plot(cs[ci], np.max(postc), 'o', markersize=10)
pl.legend(loc='lower left')
ax = pl.gca()
ax.set_xlabel('$m$')
ax.set_ylabel('$p(c|d,I)$')
ax.text(-2.8, 0.9*np.max(postc), 'max. posterior $c = %.2f$' % cs[ci], fontsize=16)
ax.text(-2.8, 0.8*np.max(postc), 'max. likelihood $\hat{c} = %.2f$' % cfit, fontsize=16)

#fig.subplots_adjust(bottom=0.12)
pl.tight_layout()
pl.show()
fig.savefig('../bayesian_line_fitting.pdf')

# do the same but using the Student's t posterior
fig.clf()
pl.close(fig)

logpost1 = np.zeros((200,200)) # using uniform prior on sigma
logpost2 = np.zeros((200,200)) # using Jeffreys prior on sigma

for i in range(200):
  for j in range(200):
    logpost1[i,j] = -0.5*(len(d)-1.)*np.log(np.sum((d-(ms[i]*x + cs[j]))**2))
    logpost2[i,j] = -0.5*(len(d))*np.log(np.sum((d-(ms[i]*x + cs[j]))**2))

# convert log posterior into posterior
post1 = np.exp(logpost1-np.max(logpost1))
post2 = np.exp(logpost2-np.max(logpost2))

# marginalise over c
post1m = np.apply_along_axis(np.trapz, 1, post1, cs)
post1m = post1m/np.trapz(post1m, ms) # normalise

# marginalise over m
post1c = np.apply_along_axis(np.trapz, 0, post1, ms)
post1c = post1c/np.trapz(post1c, cs) # normalise

# marginalise over c
post2m = np.apply_along_axis(np.trapz, 1, post2, cs)
post2m = post2m/np.trapz(post2m, ms) # normalise

# marginalise over m
post2c = np.apply_along_axis(np.trapz, 0, post2, ms)
post2c = post2c/np.trapz(post2c, cs) # normalise

fig = pl.figure(figsize=(10,5), dpi=100)

pl.subplot(1,2,1)
pl.plot(ms, postm, 'r--', label='Known $\sigma$')
pl.plot(ms, post1m, 'b-', label='Unknown $\sigma$, $p(\sigma|I) = C$')
pl.plot(ms, post2m, 'b--', label='Unknown $\sigma$, $p(\sigma|I) \propto 1/\sigma$')
pl.plot([m, m], [0, np.max(postm)], 'k--', label='True value')
ax = pl.gca()
ax.set_xlabel('$m$')
ax.set_ylabel('$p(m|d,I)$')

pl.subplot(1,2,2)
pl.plot(cs, postc, 'r--', label='Known $\sigma$')
pl.plot(cs, post1c, 'b-', label='Unknown $\sigma$, $p(\sigma|I) = C$')
pl.plot(cs, post2c, 'b--', label='Unknown $\sigma$, $p(\sigma|I) \propto 1/\sigma$')
pl.plot([c, c], [0, np.max(postc)], 'k--', label='True value')
pl.legend(loc='upper left', fancybox=True, framealpha=0.3, prop={'size': 14})
ax = pl.gca()
ax.set_xlabel('$c$')
ax.set_ylabel('$p(c|d,I)$')

pl.tight_layout()
pl.show()
fig.savefig('../bayesian_line_fitting_2.pdf')