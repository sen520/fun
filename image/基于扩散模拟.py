import numpy as np
import matplotlib.pyplot as plt
import numpy.random as npr

S0 = 100
r = 0.05
sigma = 0.25
T = 2.0
x0 = 0
k = 1.8
theta = 0.24
i = 100000
M = 50
dt = T / M


def srd_euler():
    xh = np.zeros((M + 1, i))
    x1 = np.zeros_like(xh)
    xh[0] = x0
    x1[0] = x0
    for t in range(1, M + 1):
        xh[t] = (xh[t - 1] + k * (theta - np.maximum(xh[t - 1], 0)) * dt + sigma * np.sqrt(
            np.maximum(xh[t - 1], 0)) * np.sqrt(dt) * npr.standard_normal(i))
    x1 = np.maximum(xh, 0)
    return x1

x1 = srd_euler()
plt.figure(figsize=(10, 6))
plt.hist(x1[-1], bins=30, color='#98DE2f', alpha=0.85)
plt.xlabel('value')
plt.ylabel('frequency')
plt.grid(False)

plt.figure(figsize=(12,10))
plt.plot(x1[:, :10], lw=2.2)
plt.title('Square-Root Diffusion - Simulation')
plt.xlabel('Time', fontsize=16)
plt.ylabel('Index Level', fontsize=16)
plt.show()