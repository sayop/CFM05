=============
 Problem1 - c
=============

Examine the effect of the relaxation time :math:`\tau` and the Mach number on method stability using your simulations, and compare your results to the stability criteria. Discuss how these parameters relate to the required grid size and physical time step size.


Given equation as stated in the previous section, the relaxation time is strongly coupled with kinematic viscosity :math:`\nu`.

.. math::

   \nu = \frac{2\tau - 1}{6} \Delta x

In this simulation, grid spacing and time step are consistently set to unity for various grid resolution conditions in order to avoid complexity that may arise with non-unity :math:`\Delta t` and :math:`\Delta x`. Therefore, the grid spacing doesn't change the numerics of :math:`\Delta`. Instead, to be consistent with Re=100, kinematic viscosity :math:`\nu` is to be changed, resulting in change of :math:`\tau`. The following figure illustrates the variable relaxation time allows the stable solution with different grid spacing.


.. image:: ./images/tau.png
   :width: 50%

