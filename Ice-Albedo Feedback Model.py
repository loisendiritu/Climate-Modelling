import matplotlib.pyplot as plt
import numpy as np

# Predefined ranges for L & albedo
LRange = [1150, 1350]
albedoRange = [0.15, 0.65]
L, albedo, nIters = LRange[1], albedoRange[0], 100

# Predefined variables obtained from Part I & Spreadsheet Linear Equation
albedoM = -0.01
albedoB = 2.8
sigma = 5.67E-8

# Initialize x & y lists for graph plotting
x, y = [], []

while L > LRange[0]-1:
    for i in range(1,nIters+1):
        # Guess and check loop to get temperature T & albedo
        T = L * (1 - albedo) / (4 * sigma)
        T = pow(T, 0.25)
        albedo = T * albedoM + albedoB

        # Limits albedo to the specified range of 0.15 - 0.65
        albedo = min(albedo, albedoRange[1])
        albedo = max(albedo, albedoRange[0])

        x.append(i)
        y.append(T)
    x.append(np.nan)
    y.append(np.nan)
    L -= 10

# Generate a plot temperature plotted as a function of iteration number
plt.xlabel("Iteration Number")
plt.ylabel("Temperature")
plt.title("Snowball")
plt.plot(x, y)
plt.show()
