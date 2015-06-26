#!/usr/bin/env python

"""
Show the likelihood and prior for line fitting (with known c) when different prior ranges are used.
"""

import matplotlib.pyplot as pl
import numpy as np

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)

# load data
data = np.loadtxt('linear_data_2.txt')

# x values
x = data[0]
y = data[1]

# gradietn m grid
ms = np.linspace(-5., 10., 500)

# y intercept
c = 1.

# noise with sigma = 1
sigma = 1.;

fig = pl.figure(figsize=(6,5), dpi=100)

loglike = np.zeros(500)

# prior ranges
pm1 = [0., 5]
pm2 = [-2.5, 7.5]

for i in range(500):
  loglike[i] = -np.sum(0.5*(y-(ms[i]*x + c))**2/sigma**2)

like = np.exp(loglike-np.max(loglike))
Z1 = np.trapz(like[(ms>=pm1[0]) & (ms<=pm1[1])], ms[(ms>=pm1[0]) & (ms<=pm1[1])])/np.diff(pm1)
Z2 = np.trapz(like[(ms>=pm2[0]) & (ms<=pm2[1])], ms[(ms>=pm2[0]) & (ms<=pm2[1])])/np.diff(pm2)

like = like/np.max(like)

pl.plot(ms, like, 'b', label='Likelihood')

pl.plot([pm1[0], pm1[0], pm1[1], pm1[1]], [0., 1./np.diff(pm1), 1./np.diff(pm1), 0.], 'k', 
        label='$p(m|H_3,I)$')
pl.plot([pm2[0], pm2[0], pm2[1], pm2[1]], [0., 1./np.diff(pm2), 1./np.diff(pm2), 0.], 'k--', 
        label='$p(m|H_4,I)$')

pl.legend(loc='upper right')
pl.grid(True)

ax = pl.gca()
ax.set_xlabel('$m$')
ax.set_xlim(ms[0], ms[-1])

ax.text(2, 0.55, '$\mathcal{O}_{34} = Z_3/Z_4 = %.2f$' % (Z1/Z2), fontsize=17)

Znoise = np.exp(-np.sum(0.5*y**2/sigma**2) - np.max(loglike))

s = '%.2e' % (Z1/Znoise)
ssplit = s.split('e')
ax.text(2, 0.45, '$\mathcal{O}_{32} = Z_3/Z_2 = %.1f \\times 10^{%d}$' % (float(ssplit[0]), 
        int(ssplit[1])), fontsize=17)

s = '%.2e' % (Z2/Znoise)
ssplit = s.split('e')
ax.text(2, 0.35, '$\mathcal{O}_{42} = Z_4/Z_2 = %.1f \\times 10^{%d}$' % (float(ssplit[0]), 
        int(ssplit[1])), fontsize=17)

pl.show()
fig.savefig('../occam_factor.pdf')
