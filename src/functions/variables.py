import numpy as np

class domainVars:
   x = []
   y = []
   dx = 0.0
   dy = 0.0
   Lref = 0.0

class flowVars:
   Uref = 0.0
   nu = 0.0     # kinematic viscosity
   Re = 0.0     # Reynolds number
   rho = []       # kinematic pressure: used for both dimensional and non-dimensional forms
   u = []       # u velocity: used for both dimensional and non-dimensional forms
   v = []       # v velocity: used for both dimensional and non-dimensional forms

class timeVars:
   dt = 0.0
   t = 0.0

class LBM:

   c  = 0.0
   cs = 0.0
   tau = 0.0
   ei = [None] * 2
   wi = [None] * 1
   fi = [None] * 9
   fieq = [None] * 9
