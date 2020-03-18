"""
A stochastic indicator used on trading stocks. Designed as part of project Analyzing Trading Signals
"""

# Modules used
import pandas as pd
import matplotlib.pyplot as plt

#downloads data into a DataFrame
df = pd.read_csv('GOLD.csv', header=0)

#Create the "Lowest_14" column in the DataFrame
#" Lowest_14" is set to the lowest value for every 14 values
df[Lowest_14] = df['Low'].rolling(window=14).min()

#Create the " Highest_14" column in the DataFrame
#" Highest_14" is set the highest value for every 14 values
df[Highest_14] = df['High'].rolling(window=14).max()

#Create the "%K" column in the DataFrame
df['%K'] = 100*((df['Close'] - df[Lowest_14]) / (df[Highest_14] - df[Lowest_14]) )

#Create the "%D" column in the DataFrame
df['%D'] = df['%K'].rolling(window=3).mean()

# Plots the close price on the first subplot
plt.subplot(211)
plt.plot(df['Close'])

# Add title and axis names
plt.title('Closing Price')
plt.grid()

# Plots %K & %D on the second subplot
plt.subplot(212)
plt.plot(df['%K'], label='%K')
plt.plot(df['%D'], label='%D')

# Add title and axis names
plt.title('Stochastic Oscillator')
plt.legend()
plt.grid()
plt.show()