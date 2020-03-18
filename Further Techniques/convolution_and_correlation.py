"""
signal_analysis_convolution.py - This script calculates the convolution of two trading signals
"""
# Necessary Libraries
import numpy as np
from scipy import fftpack, signal
import pandas as pd
import matplotlib.pyplot as plt

# Importing signals
sig1_df = pd.read_csv('trading_data_sig2_A.csv', header=0)
sig2_df = pd.read_csv('trading_data_sig2_B.csv', header=0)

# Converting to numpy array
sig1_y = sig1_df['F(N)']
sig2_y = sig2_df['F(N)']

# Using the convolve and correlate functions
sig_conv = signal.convolve(sig1_y, sig2_y)
sig_corr = signal.correlate(sig1_y, sig2_y)

# Plotting results
fig, axs= plt.subplots(2,2)
(signal1, signal2), (conv, corr) =axs
signal1.plot(sig1_y)
signal2.plot(sig2_y)
conv.plot(sig_conv)
corr.plot(sig_corr)
plt.show()