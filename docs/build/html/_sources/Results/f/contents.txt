=============
 Problem1 - f
=============

Repeat parts b and c for the case of :math:`H=1.5W` (except for validation).

---------
 Re = 100
---------

- NxN = 40x60

.. image:: ./images/Re100/strm_40x60.png
   :width: 40%

<Streamlines for 40x60 case>

.. image:: ./images/Re100/uVel_40x60.png
   :width: 40%

<Centerline u-velocity compared with Ghia's numerically resolved data>

.. image:: ./images/Re100/vVel_40x60.png
   :width: 40%

<Centerline v-velocity compared with Ghia's numerically resolved data>


  - **Observations**

    - In Re=100, the main vortex is formed in a very similar distance from the lid location. 
    - Because of fixed viscosity even in the long depth, the momentum transferred from the moving lid penetrates by the same amount, so it is observed that the vortex is created in a very same way as the previous domain configuration.
    - This observation can be confirmed qualitatively in the centerline u-velocity plot: The curved shape is shifted upward.
    - However, in the bottom clock-counterwise rotating vortices are observed on both bottom corners.

|

---------
 Re = 500
---------

- NxN = 160x240

.. image:: ./images/Re500/strm_160x240.png
   :width: 40%

<Streamlines for 160x240 case under higher Resolution number condition>

  - **Observations**

    - Higher resolution condition makes numerical solution unstable: The required grid spacing needs to be small enough to have stable solution. This case running took a couple of hours with current Python script.
    - There is distinctive layer separation in between two counter-rotating vortices: This was identically observed in the previous homework problems under the same condition.
