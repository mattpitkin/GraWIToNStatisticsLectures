#!/usr/bin/env python

"""
Make plot of data containing a line with Gaussian noise (not showing the best fit)
"""

import matplotlib.pyplot as pl
import numpy as np

# x values
x = np.linspace(-5, 5, 8)

# gradient
m = 0.75

# y intercept
c = 1.

# line
y = m*x + c

# noise with sigma = 1
sigma = 1.
n = sigma*np.random.randn(len(x))

d = y + n # the x "data"

# output the data for later use (in integration)
np.savetxt('linear_data_2.txt', np.vstack((x, d)), fmt='%.9f')

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=150)

# plot data points line + noise
pl.plot(x, d, 'bx', markersize=12, mew=1.5, label='$x$ data, $\sigma^2=1$')

pl.grid(True)
pl.legend(loc='upper left')
ax = pl.gca()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.subplots_adjust(bottom=0.12)

pl.show()
fig.savefig('../linear_data_2.pdf')

