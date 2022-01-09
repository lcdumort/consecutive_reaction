import numpy as np  # numerical library
import matplotlib.pyplot as plt  # graph-plottig library

# Set up the data
k1 = 1
k2 = 2
conc_A_0 = float(10)

time = np.arange(0.0, 5.0, 0.001)

conc_A = conc_A_0 * np.exp(-k1*time)
conc_B = conc_A_0 * (k1/(k2-k1))*(np.exp(-k1*time)-np.exp(-k2*time))
conc_C = conc_A_0 * (1 + (1/(k2-k1))*(k1 * np.exp(-k2 * time) - k2 * np.exp(-k1 * time)))


# plot the data
fig, ax = plt.subplots()

ax.plot(time, conc_A, label='concentration A')
ax.plot(time, conc_B, label='concentration B')
ax.plot(time, conc_C, label='concentration C')

ax.set_ylabel('concentration (mol/l)')
ax.set_xlabel('time (s)')
ax.legend()

plt.show()
