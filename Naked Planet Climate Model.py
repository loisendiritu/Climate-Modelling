import numpy as np
import matplotlib.pyplot as plt

timestep = 100 #years
waterdepth = 4000 #meters
L = 1350 #watts/m2
albedo = 0.3
epsilon = 1
sigma = 5.67E-8
 
heatcapacity = waterdepth * 4.2E6 #J/K m2
timeyears = [0]
TK = [0]
heatcontent = heatcapacity * TK[0]
heatin = L * ((1 - albedo)/4)
heatout = 0

for i in range(0,100):
	timeyears.append ( timestep + timeyears[-1])
	heatout = epsilon * sigma * pow(TK[-1],4)
	print(TK[-1], heatout)
	heatcontent = heatcontent + (heatin - heatout) * timestep * 3.14E7
	TK.append (heatcontent / heatcapacity)
	print(i, timeyears[-1])
print(TK[-1])
plt.plot(timeyears, TK)
plt.show()

	



