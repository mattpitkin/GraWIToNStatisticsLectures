#!/usr/bin/env python

"""
Create a sine wave in Gaussian noise and compare the Bayesian spectral estimation to a power spectrum
"""

import matplotlib.pyplot as pl
import matplotlib.mlab as mlab
import matplotlib.gridspec as gridspec
import numpy as np

# set plot to render labels using latex
pl.rc('text', usetex=True)
pl.rc('font', family='serif')
pl.rc('font', size=14)

# times
t = np.linspace(0., 1., 100)

# set up signal to inject
f = 25.43 # Hz
phi = 2.1 # radians
A = 1.0 # amplitude

# sinewave
y = A*np.sin(2.*np.pi*f*t + phi)

# noise with sigma = 1
sigma = 1.;
n = np.random.randn(len(t))

d = y + n # the "data"

fig = pl.figure(figsize=(12,6), dpi=100)

gs = gridspec.GridSpec(1, 2, width_ratios=[1,2])

pl.subplot(gs[0])

# plot data
pl.plot(t, d, 'bo')
pl.plot(t, y, 'k-')
ax = pl.gca()
ax.set_xlabel('time (seconds)')

# get posterior on frequency
freqs = np.linspace(0., 1./(2.*(t[1]-t[0])), 200)
logpost1 = np.zeros(len(freqs))
logpost2 = np.zeros(len(freqs))

# get sums in posterior
d2 = np.sum(d**2)

for i in range(200):
  R = np.sum(d*np.cos(2.*np.pi*freqs[i]*t))
  I = np.sum(d*np.sin(2.*np.pi*freqs[i]*t))
  #print 2.*(R**2+I**2), d2
  logpost1[i] = -0.5*(len(d)-2)*np.log(1.-2.*(R**2 + I**2)/(len(d)*d2))

  logpost2[i] = (R**2 + I**2)/sigma**2

# convert log posterior into posterior
post1 = np.exp(logpost1-np.max(logpost1))
post1 = post1/np.trapz(post1, freqs)

post2 = np.exp(logpost2-np.max(logpost2))
post2 = post2/np.trapz(post2, freqs)

# get power spectrum
pxx, pfreqs = mlab.psd(d, NFFT=len(d), Fs=(1./(t[1]-t[0])), detrend=mlab.detrend_none,
    window=mlab.window_none, noverlap=0, pad_to=None, sides='default', scale_by_freq=None)

# normalise posteriors to the same height as the power spectrum
if np.max(post1) > np.max(post2):
  pxx = pxx*(np.max(post1)/np.max(pxx))
else:
  pxx = pxx*(np.max(post2)/np.max(pxx))

pl.subplot(gs[1])
pl.plot(freqs, post1, 'b', label='$p(f|d,I)$ for unknown $\sigma$')
pl.plot(freqs, post2, 'b--', label='$p(f|d,I)$ for known $\sigma$')
pl.plot(pfreqs, pxx, 'r-o', label='Power spectrum')
pl.plot([f, f], [0., np.max(pxx)], 'k--', label='True frequency')
pl.legend(loc='upper left', fancybox=True, framealpha=0.3, prop={'size': 14})
ax = pl.gca()
ax.set_xlabel('Frequency (Hz)')
ax.set_yticklabels([])
ax.set_ylim(0., np.max(pxx))

pl.tight_layout()
pl.show()
fig.savefig('../spectral_estimation.pdf')