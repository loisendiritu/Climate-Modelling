import numpy as np
import matplotlib.pyplot as plt

nX = 10
domainWidth = 1e6
dx = domainWidth/nX
timeStep = 100
nYears = 20000
nSteps = int(nYears/timeStep)
flowParam = 1e4
snowFall = 0.5
plotLimit = 4000

elevations = np.zeros(nX+2)
flows = np.zeros(nX+1)

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
