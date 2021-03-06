#!/usr/bin/env python

"""
Make plot of data containing a line with Gaussian noise
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
n = np.random.randn(len(x))

d = y + n # the x "data"

# get the least squares fit values for m and c
mfit, cfit = np.linalg.lstsq(np.vstack([x, np.ones(len(x))]).T, d)[0]
yfit = mfit*x + cfit

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=150)

# plot data points line + noise
pl.plot(x, d, 'bx', markersize=14, mew=2, label='$x$ data')
pl.plot(x, y, 'k-', label='True line')
pl.plot(x, yfit, 'r-', label='Best fit line')

# plot residuals
for i, xv in enumerate(x):
  pl.plot([xv, xv], [yfit[i], d[i]], 'r-.')

pl.grid(True)
pl.legend(loc='upper left')
ax = pl.gca()
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')

fig.subplots_adjust(bottom=0.12)

pl.show()
fig.savefig('../linear_data.pdf')
