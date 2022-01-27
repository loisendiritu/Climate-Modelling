# The Naked Planet Climate Model
The naked planet climate model is an energy balance model. Energy from the sun comes in at a particular rate, and energy flows out at a rate which is dependent on the temperature of the planet.
The temperature of the planet is determined by balancing energy fluxes in and out of the planet.  Incoming solar heat is determined by L * (1-albedo) / 4, and outgoing infrared is calculated as epsilon * sigma * T^4.

The goal of this project is to numerically simulate how the planetary temperature of a naked planet would change through time as it approaches equilibrium i.e. the state at which it stops changing. The planet starts with some initial temperature. "Naked" means that we are not accounting for the atmospheric layers that cause the greenhouse effect.

The “heat capacity” (units of Joules / m2 K) of the planet is set by a layer of water which absorbs heat and changes its temperature.  If the layer is very thick, it takes a lot more heat (Joules) to change the temperature.

The heat content is related to the temperature by the heat capacity. The numerical method in this project is to take time steps, extrapolating the heat content from one step to the next using the incoming and outgoing heat fluxes.

# Iterative Runaway Ice-Albedo Feedback Model
Albedo refers to the fraction of light that gets reflected back into space. The higher the albedo of the planet, the colder the planet. Ice-albedo feedback is a positive feedback in the climate system.

Define and initialize variables for the number of iterations, and for epsilon and sigma. Also set up variables for the range of L values over which you are going to do the calculation. Each pass over the range in L values requires two nested loops, the outer one over values of L, and the inner one for the iterations.

# Ice Sheet Flow Model
Ice itself flows very slowly due to its high viscosity. The force driving the flow is the differences in pressure in the interior of the ice, which arise from differences in the elevation of the ice surface.  If you make a pile of ice, it will flow outward and flatten itself out.

The model is formulated in one dimension, on a horizontal grid.  Start with 10 grid cells.  Let them span a horizontal distance of 1000 km, or 10^6 meters.  Each grid cell will have an elevation of ice.  Flow between adjacent cells depends on the difference between their elevations.  Snow falls equally on all grid cells. Assume that the ice sheet is confined to a landmass like Greenland or Antarctica, so that the thickness of the ice at the boundaries has to be zero.  Ice flows into the ocean and disappears, both in reality and in this model.

The model steps forward in time, using a time step of 100 years.  It will begin to rise uniformly, but the elevations at the edges will be eroded by flow to the ocean.  Eventually it will reach a steady state, where snowfall in each grid cell is balanced by flow from the grid cell, which is all determined by the slope of the ice surface.  
