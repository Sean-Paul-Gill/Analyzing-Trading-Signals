"""
autocorrelation_sig2.py: The following script generates a CSV data-set that is Auto-correlated. Specifications:
    - Sig2_A.csv depends on the current rising state and rises/drops the trade a random amount between 0,20
    - Sig2_B.csv is in the inverse rising state as A and rises/drops the trade a random amount between 0,20
    - The signals are outputted as a comma-separated CSV file.
The behaviour of this script is similar to competitive markets such as Playstation and XBOX, where when one market
is rising, the other is generally dropping and vice versa.
"""

from numpy import random, arange

# Defining the Parameters
length, step = 10, 0.01
N, F_N_A, F_N_B = [], [], []
start_trade_value = 200
rising_state, rising_states = True, []
print("Generating Autocorrelated Data...\n")
print("Length: ", length, " Step-Size: ", step)
print("Initial Trade Value: ", start_trade_value, "\n")

# Declaring Trading signal
F_N_A.append(start_trade_value)
F_N_B.append(start_trade_value)
for i in arange(0,length+step,step):
    N.append(round(i, 2))

    # Defining the Rising/Falling value
    F_N_Deviation_Low = random.uniform(-20, 0)
    #F_N_Deviation_High = random.uniform(0, 20)
    F_N_Deviation_High = random.uniform(0, 20)

    rising_state = random.choice([rising_state, not rising_state], p = [0.80, 0.20])
    rising_states.append(rising_state)
    print("Trade is Rising: ", rising_state)

    if rising_state == True:
        F_N_A.append(F_N_A[int(i/step)]+F_N_Deviation_High)
        F_N_B.append(F_N_B[int(i/step)]+F_N_Deviation_Low)
    else:
        F_N_A.append(F_N_A[int(i / step)] + F_N_Deviation_Low)
        F_N_B.append(F_N_B[int(i / step)] + F_N_Deviation_High)

# Deleting last element to ensure N & F_N and same length
del F_N_A[-1], F_N_B[-1]

# Appending the results to a CSV
f_a = open("trading_data_sig2_A.csv", "w")
f_b = open("trading_data_sig2_B.csv", "w")
for i in range(len(N)):
    f_a.write("{},{}\n".format(N[i], F_N_A[i]))
    f_b.write("{},{}\n".format(N[i], F_N_B[i]))
f_a.close()