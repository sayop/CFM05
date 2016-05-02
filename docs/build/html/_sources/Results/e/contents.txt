=============
 Problem1 - e
=============

Discuss how the simulation speed depends on the grid resolution and time step.


The simulation for different grid resolutions were conducted with consistent convergence criterion as 0.01 % of normalized residual. The evolution of u-velocity residual with different grid spacing is placed on top of each other in the following plot. As the grid spacing become smaller, the more time integration was required to achieve the pre-specified convergence criterion. It also means the more grid points requires more computational time, which is illustrated as shown in the second figure.


- Effect of grid spacing on the convergence  history

  .. image:: ./images/u-residual.png
     :width: 50%


- Effect of grid spacing on the computational time to achieve the steady solution.

  .. image:: ./images/computeTime.png
     :width: 50%
