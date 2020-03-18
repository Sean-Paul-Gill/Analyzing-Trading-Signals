"""
Fast Fourier Transform (FFT) to compute the spectral density of a signal. 
The spectrum represents the energy associated to frequencies (encoding periodic fluctuations in a signal). 
It is obtained with a Fourier transform, which is a frequency representation of a time-dependent signal. 
A signal can be transformed back and forth from one representation to the other with no information loss.
"""

# Necessary Libraries
import numpy as np
from scipy import fftpack, signal
import pandas as pd
import matplotlib.pyplot as plt

# Reading the generated data signal in CSV format
df = pd.read_csv('test_sig_1.csv', header=0)

# Setting Number of Samples and Period
N = len(df)
T = (df.iloc[-1][0]-df.iloc[0][0])/(N-1)
print("Numbers of Samples (N):", N, " | Sampling Interval (T):", T)

# Obtaining the Values as a Numpy Array from the Dataframe
x = df['N'].values
y = df['F(N)'].values
DC_offset = y.mean()
print("Current DC Offset:", DC_offset)

# Removing the DC offset from the signal
y = y - DC_offset


# Computing Fast Fourier Transform of Signal N, F(N)
xf = fftpack.fftfreq(N) / T
yf = fftpack.fft(y) * (2.0/N)

# Setting the plotting parameters
xf_plot, yf_magplot, yf_phaseplot = np.linspace(0.0, 1.0/(2*T), num=N//2),
np.abs(yf[:N//2]), np.angle(yf[:N//2])

# Plotting Time Domain & Frequency Domain (Magnitude and Phase)
fig, (time, freq, phase) = plt.subplots(3, 1)
time.plot(x, y), freq.plot(xf_plot, yf_magplot), phase.plot(xf_plot, yf_phaseplot)
time.set_xlabel('Time Interval (N)'), time.set_ylabel('Stock Market Value')
freq.set_xlabel('Frequency in Hertz (Hz)'), freq.set_ylabel('Spectrum Magnitude')
phase.set_xlabel('Frequency in Hertz (Hz)'), phase.set_ylabel('Phase in Radians (radians)')
plt.show()

# Periodogram with different window methods
f_s = 1/0.01
windows = ['hamming', 'boxcar', 'blackman', 'bartlett', 'hanning']
for w in windows:
    f, P = signal.periodogram(x, f_s, window=w, scaling='spectrum')
    plt.semilogy(f, P, label=w+' function')
plt.legend()
plt.show()

# Reconstructing Sinusoidal Signal
y_recon = fftpack.ifft(yf) / (2.0/N)

# Comparing the original VS reconstructed
plt.plot(x, y_recon, label='Reconstructed Signal'), plt.plot(x, y, label='Original Signal')
plt.legend()
plt.show()