"""
Using a common LPC algorithm that is used in speech prediction and speech analysis. It's essentially a regressor that predicts the next value of a trade based on
previous data. This can be seen as a machine learning algorithm in a way
"""

import numpy as np
from scipy import fftpack, signal
import pandas as pd
import matplotlib.pyplot as plt

def lpc(y, m):
#Return m linear predictive coefficients for sequence y using Levinson-Durbin prediction algorithm
    # step 1: compute autoregression coefficients R_0, ..., R_m
    R = [y.dot(y)]
    if R[0] == 0:
        return [1] + [0] * (m-2) + [-1]
    else:
        for i in range(1, m + 1):
            r = y[i:].dot(y[:-i])
            R.append(r)
        R = np.array(R)

        # step 2:
        A = np.array([1, -R[1] / R[0]])
        E = R[0] + R[1] * A[1]
        for k in range(1, m):
            if (E == 0):
                E = 10e-17
            alpha = - A[:k+1].dot(R[k+1:0:-1]) / E
            A = np.hstack([A,0])
            A = A + alpha * A[::-1]
            E *= (1 - alpha**2)
    return A
    
# Importing Necessary Libraries
from pandas import read_csv
from signal_analysis_functions import lpc
import numpy as np
import matplotlib.pyplot as plt

# Importing the Trading Signal and obtaining the numpy array
df = read_csv('Discrete_SW_2.csv', header=0)
x, y = df['N'].values, df['F(N)'].values

# Importing the future values of Discrete_Autocorrelated_1: 9.0-10.0
df_extended = read_csv('appended_sw.csv', header=0)
y_future = df_extended['F(N)'].values

# Plotting the Original Signal
plt.plot(y)
plt.show()

predicted_values = []
for i in range(len(y_future)):
    # Obtaining the LPC coefficients for m samples
    m = 5
    lpc_coefficients = -1*lpc(y, m)
    
    # Cleaning up LPC coefficients array
    lpc_coefficients = np.delete(lpc_coefficients, 0)
    lpc_coefficients = np.flip(lpc_coefficients)
    lpc_coefficients = np.round(lpc_coefficients, 8)
    print("The LPC coefficients: ", lpc_coefficients)
    
    # Taking last m samples and predicting next value using co-efficients
    last_values = y[-m:]
    print("These last 5 values: ", last_values)
    next_value = np.sum(np.multiply(lpc_coefficients, last_values))
    predicted_values.append(next_value)
    print("Predicted Value", next_value)
    print("")
    y = np.append(y, y_future[i])
    
# Exporting data to csv
from pandas import DataFrame
pd.DataFrame(predicted_values).to_csv("predicted.csv", index=False)