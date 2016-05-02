=============
 Problem1 - a
=============

Describe the essential steps of the solution method. Include the discretized equations and implementation of boundary conditions.

This project aims to use Lattice Boltzmann Method for solving the lid driven flow problem and assess its prediction accuracy and several numerical issues as stated in the problem description. In this project, D2Q9 latice is employed to describe the stream the distribution fuctions along the specified directions. The directions in which 9-bit lattice BGK model evoloves defines following 9 discrete velocities:

.. math::

   e_{i} = \left\{\begin{matrix} (0,0) & i=0\;\;\;\;\;\;\;\;\;\; & \\  (\text{cos}[(i-1)\pi/2],\text{sin}[(i-1)\pi/2]) & i=1,2,3,4 & \\ \sqrt{2}(\text{cos}[(i-5)\pi/2 + \pi/4], \text{sin}[(i-5)\pi/2 + \pi/4]) & i=5,6,7,8 & \end{matrix}\right.


.. image:: ./images/d2q9.png
   :align: center
   :width: 30%

Along the defined direction, 9 independent fluid particles are moved and re-located then update their distribution function in time. The evolution equation of the density distribution function is integrated in time:

.. math::

   f_{i}(x_{i}+ce_{i}\Delta t, t+\Delta t) - f_{i}(x_{i}, t) = - \frac{1}{\tau} \left [ f_{i}(x_{i},t) - f_{i}^{\text{eq}}(x_{i},t) \right ]

where :math:`c=\Delta x / \Delta t`, and :math:`\Delta x` and :math:`\Delta t` are the lattice spacing and the time step, respectively. Here, :math:`\tau` is the dimensionless relaxation time that approximates the temporal rate at which instantaneous distribution function evolves and transitions to the equilibrium states. And the :math:`f_{i}^{\text{eq}}` expresses the equilibrium density function, which is determined by:

.. math::

   f_{i}^{\text{eq}}(x_{i},t) = \omega_{i}\rho + \rho s_{i}(u_{i}(x_{i},t))

where

.. math::

   s_{i} (u_{i}) = \omega_{i} \left [ e\frac{(e_{i}u_{i})}{c} + 4.5 \frac{(e_{i}u_{i})^{2}}{c^{2}} - 1.5 \frac{u_{i}u_{i}}{c^{2}}\right ]

with the weight coefficient:

.. math::

   \omega_{i} = \left\{\begin{matrix} \frac{4}{9} & i = 0\;\;\;\;\;\;\;\;\;\; \\  \frac{1}{9} & i = 1,2,3,4 \\  \frac{1}{36} & i = 5,6,7,8 \end{matrix}\right.


After updating the distribution function, we are then to find fluid density and velocity from the integrated distribution function by assuming the relationship between the distribution function and macroscopic fluid properties:


