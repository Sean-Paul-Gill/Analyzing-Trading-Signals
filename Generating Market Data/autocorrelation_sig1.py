"""
autocorrelation_sig1.py: This script generates an autocorrelated signal based on the previous rising state. The rising
state will have a low probability of change (20% for the rising_state to inverse).
The output will be in the form of a comma-separated CSV file. The behaviour of the data is very similar to Market
Data and can be seen when you use a simple plotting function.
"""

from numpy import random, arange

# Defining the Parameters
length, step = 10, 0.01
N, F_N = [], []
start_trade_value = 200
rising_state, rising_states = True, []
print("Generating Autocorrelated Data...\n")
print("Length: ", length, " Step-Size: ", step)
print("Initial Trade Value: ", start_trade_value, "\n")

# Declaring Trading signal
F_N.append(start_trade_value)
for i in arange(0,length+step,step):
    N.append(round(i, 2))

    # Defining the Rising/Falling value
    F_N_Deviation_Low = random.choice([random.uniform(-20, 0), random.uniform(-300, -100)], p = [0.95, 0.05])
    F_N_Deviation_High = random.choice([random.uniform(0, 20), random.uniform(100, 300)], p = [0.95, 0.05])

    rising_state = random.choice([rising_state, not rising_state], p = [0.80, 0.20])
    rising_states.append(rising_state)
    print("Trade is Rising: ", rising_state)

    if rising_state == True:
        F_N.append(F_N[int(i/step)]+F_N_Deviation_High)
    else:
        F_N.append(F_N[int(i / step)] + F_N_Deviation_Low)

# Deleting last element to ensure N & F_N and same length
del F_N[-1]

# Appending the results to a CSV
f = open("trading_data_sig1.csv", "w")
for i in range(len(N)):
    f.write("{},{}\n".format(N[i], F_N[i]))
f.close()