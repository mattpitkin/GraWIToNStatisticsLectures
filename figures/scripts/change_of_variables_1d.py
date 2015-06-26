#!/usr/bin/env python

"""
Show distribution after a change of variables with y = x^(1/2), where the pdf for x is Gaussian
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
import numpy as np

# normal distribution
mu = 5. # the mean, mu
sigma = 1 # standard deviations, sigma

x = np.linspace(0, 10, 1000) # x

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

# plot pdfs
pl.plot(x, norm.pdf(x, mu, sigma), 'b--', label='$p(z=x)$')
pl.plot(np.sqrt(x), 2.*np.sqrt(x)*norm.pdf(x, mu, sigma), 'r', label='$p(z=y=x^{1/2})$')

ax = pl.gca()
ax.set_xlabel('$z$', fontsize=14)
ax.set_ylabel('$p(z)$', fontsize=14)

ax.legend(loc='upper right', frameon=False)

fig.subplots_adjust(bottom=0.15)

pl.savefig('../change_of_variables_1d.pdf')
pl.show()

