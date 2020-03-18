"""
Bollinger Bands - Applying a common trading technique but harnessing the use of the Savitzsky Golay Filter
"""

# Necessary Libraries
import numpy as np
from scipy import fftpack, signal
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Reading the generated data signal in CSV format
df = pd.read_csv('test_sig_3.csv', header=0)

# Setting Number of Samples and Period
N = len(df)
T = (df.iloc[-1][0]-df.iloc[0][0])/(N-1)
print("Numbers of Samples (N):", N, " | Sampling Interval (T):", T)

# Obtaining the Values as a Numpy Array from the Dataframe
x = df['N'].values
y = df['F(N)'].values
print("Current DC Offset:", y.mean())

# Computing Fast Fourier Transform of Signal N, F(N)
xf = fftpack.fftfreq(N) / T
yf = fftpack.fft(y) * (2.0/N)

# Setting the plotting parameters
xf_plot, yf_magplot, yf_phaseplot = np.linspace(0.0, 1.0/(2*T), num=N//2), np.abs(yf[:N//2]),
np.angle(yf[:N//2])

# Reconstructing Sinusoidal Signal
y_recon = fftpack.ifft(yf) / (2.0/N)

# Run the given data through the Savitzky-Golay Filter
filtered = savgol_filter(y, 101, 1)

# Create an array to place the different anomalies outside the bands
anom = []
array1 = []

# Outlier array to get the specific points where the anomalies occur
outlier_array = []

# Run through the signals to find the error in difference between SGF and input signal
for i in range(len(filtered)):
    array1.append(abs(filtered[i] - y[i]))

# Find the standard deviation of the previously calculated error
std_1 = np.std(array1)

# Get the two bands
ball1,ball2 = filtered+(3.4*std_1),filtered-(3.4*std_1)

# Run through the filtered and add elements into the anomaly array
for i in range(len(filtered)):
    if y[i] > ball1[i]:
        anom.append(y[i])
        outlier_array.append(i)
    elif y[i] < ball2[i]:
        anom.append(y[i])
        outlier_array.append(i)
    else:
        anom.append(float('nan'))
print (outlier_array)

# Plot all information
plt.plot(y, label='Apple Share Prices(2014-2019)')
plt.plot(anom,'bo', label='Anomalies')
plt.plot(filtered, label='Savitzky-Golay Signal')
plt.plot(ball1, label='Upper Bollinger Band',color='green')
plt.plot(ball2, label='Lower Bollinger Band' ,color='green')
plt.title('Bollinger Bands Anomaly Detection using 3.4 standard deviations')
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.legend()
plt.show()