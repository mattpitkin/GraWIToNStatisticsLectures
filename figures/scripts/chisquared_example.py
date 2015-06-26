#!/usr/bin/env python

"""
Make plots of the chi-squared distribution given some fake power spectrum data
"""

import matplotlib.pyplot as pl
from scipy.stats import norm
from scipy.stats import chi2
import numpy as np
import os

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)
fig = pl.figure(figsize=(6,5), dpi=100)

nud = 24. # number of degrees of freedom of data
sigmad = np.sqrt(2.*nud) # standard deviation of data

N = 15 # number of samples
nu = N-1 # number of degrees of freedom
sigma = 2. # standard devaition on measurements

# create a short frequency series power spectrum using chi-squared distribution
if os.path.isfile('chisquared_data.txt'):
  # use previously created data if it exists
  data = np.loadtxt('chisquared_data.txt')
else:
  data = chi2.rvs(nud, size=N)
  np.savetxt('chisquared_data.txt', data, '%.5f')

# add a small spike into one frequency bin
data[7] = 55.

# plot spectrum
pl.errorbar(range(1,N+1), data, yerr=sigmad, fmt='o')
ax = pl.gca()
ax.set_xlabel('Frequency bin', fontsize=14)
ax.set_ylabel('Power spectral density', fontsize=14)
ax.text(8.9, 60., '$\hat{\mu} = \\frac{1}{15}\sum x_i = %.1f$' % np.mean(data), fontsize=18,
        bbox={'facecolor': 'none', 'pad':14, 'ec': 'r'})   
fig.subplots_adjust(bottom=0.15)
pl.savefig('../chisquared_data.pdf')
pl.show()
fig.clf()
pl.close(fig)

# new figure
fig = pl.figure(figsize=(10,5), dpi=100)

# get the chi-squared value from the data
chisq = np.sum((data - np.mean(data))**2/(sigmad**2))

x = np.linspace(0., 50., 1000) 
c2pdf = chi2.pdf(x, nu)

# plot chi-squared pdf
pl.plot(x, c2pdf)
pl.plot([chisq, chisq], [0, np.max(c2pdf)], 'k--')

pl.fill_between(x, np.zeros(len(x)), c2pdf, where=x>=chisq, alpha=0.6, facecolor='green', interpolate=True)
ax = pl.gca()
ax.set_xlabel('$\chi^2$', fontsize=14)
ax.set_ylabel('$p(\chi^2)$', fontsize=14)
ax.text(chisq+2, 0.07, '$p_{14}(\chi^2) = %.2f$' % chisq, fontsize=16)

# cumulative function
c2cdf = chi2.cdf(x, nu)
pvalue = 1.-c2cdf[x<=chisq][-1]
print pvalue
ax.text(chisq+2, 0.05, '$p{\\rm -value} = %.2f$' % pvalue, fontsize=16,
        bbox={'facecolor': 'none', 'pad':12, 'ec': 'r'})

fig.subplots_adjust(bottom=0.15)

pl.savefig('../chisquared_pdf.pdf')
pl.show()

