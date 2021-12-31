import numpy as np
import matplotlib.pyplot as plt

# Define Constants
nX = 10                       # number of grid points
domainWidth = 1e6             # meters
dx = domainWidth/nX           # meters
timeStep = 100                # years
nYears = 20000                # years
nSteps = int(nYears/timeStep) 
flowParam = 1e4               # m horizontal /yr
snowFall = 0.5                # m / y
plotLimit = 4000              # meters

# Initialize elevations and flows
elevations = np.zeros(nX+2)
flows = np.zeros(nX+1)

# Set up plotting
fig, ax = plt.subplots()
ax.plot(elevations)
ax.set_ylim([0, plotLimit])
plt.show(block=False)

for iTime in range(0, nSteps):
    for ix in range(0, nX+1):
        flows[ix] = (elevations[ix]-elevations[ix+1])/dx * flowParam * (elevations[ix] + elevations[ix+1])/2/dx

    for ix in range(1, nX+1):
        elevations[ix] = elevations[ix] + (snowFall + flows[ix-1] - flows[ix]) * timeStep


    print("year", iTime*timeStep)
    ax.clear()
    plt.plot(elevations)
    ax.set_ylim([0, plotLimit])
    plt.draw()
    plt.pause(0.05)

    

ax.clear()
ax.plot(elevations)
ax.set_ylim([0, plotLimit])
plt.show()
fig.canvas.draw()
