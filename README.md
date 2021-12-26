# The Naked Planet Climate Model
The naked planet climate model is an energy balance model. Energy comes in at a particular rate, and energy flows out at a rate which is dependent on the temperature of the planet.
The temperature of the planet is determined by balancing energy fluxes into and out of the planet.  Incoming solar heat is determined by L * (1-albedo) / 4, and outgoing infrared is calculated as epsilon * sigma * T^4.

The goal is to numerically simulate how the planetary temperature of a naked planet would change through time as it approaches equilibrium (the state at which it stops changing).  The planet starts with some initial temperature. "Naked" means that we are not accounting for the atmospheric layers that cause the greenhouse effect.

The “heat capacity” (units of Joules / m2 K) of the planet is set by a layer of water which absorbs heat and changes its temperature.  If the layer is very thick, it takes a lot more heat (Joules) to change the temperature.

The heat content is related to the temperature by the heat capacity. The numerical method is to take time steps, extrapolating the heat content from one step to the next using the incoming and outgoing heat fluxes.
