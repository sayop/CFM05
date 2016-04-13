#!/usr/bin/env python
import sys
import numpy as np
import time
from post import *

#
# simulation parameters
#
# domain parameters
Lx = 100
Ly = 100

dy = dx = 1
dt = 1
imax = Lx / dx + 1
jmax = Ly / dy + 1
x = np.zeros(imax)
y = np.zeros(jmax)
for i in range(imax):
   x[i] = 0.0 + dx * i
for j in range(jmax):
   y[j] = 0.0 + dy * j

maxIter = 100
nIterWrite = 100



# flow characteristics
Re = 100.0
Utop = 0.1
nu = Utop * Lx / Re

#
# LBM parameters
#
tau = 0.5 * (6.0 * nu * dt / (dx ** 2) + 1.0)
c = dx / dt
cs = c / np.sqrt(3.0)
ei = [None] * 2
ei[0] = np.zeros(9)
ei[1] = np.zeros(9)
# define ei vector
ei[0][1] = 1
ei[0][3] = -1
ei[0][5] = 1
ei[0][6] = -1
ei[0][7] = -1
ei[0][8] = 1

ei[1][2] = 1
ei[1][4] = -1
ei[1][5] = 1
ei[1][6] = 1
ei[1][7] = -1
ei[1][8] = -1

# Setup weight coefficient, w_i
wi = np.zeros(9)

wi[0] = 4.0 / 9.0
wi[1] = 1.0 / 9.0
wi[2] = 1.0 / 9.0
wi[3] = 1.0 / 9.0
wi[4] = 1.0 / 9.0
wi[5] = 1.0 / 36.0
wi[6] = 1.0 / 36.0
wi[7] = 1.0 / 36.0
wi[8] = 1.0 / 36.0

# print out
print "## Important parameters ##"
print "Re = ", Re
print "Nu = ", nu
print "tau = ", tau
print "LBM streaming speed, c = ", c
print "LBM speed of sound, Cs = ", cs

# Initialization
print '# Initializing flow variables...'
rho = np.ones((imax,jmax))
u   = np.zeros((imax,jmax))
v   = np.zeros((imax,jmax))
# Initialize distribution function
fi   = np.ones((imax,jmax,9))

# Set boundary condition
u[:,jmax-1] = Utop

nIter = 0
t = 0.0
while True:
   nIter += 1
   t += dt

   ### Streaming ###
   ftmp = fi
   # first, move streaming particles only if there is a lattice to receive the particle.
   # Otherwise, let it empty and it will be treated properly with bounce-back scheme later.
   for j in range(jmax):
      for i in range(imax):
         for n in range(9):
            inew = int(i + ei[0][n])
            jnew = int(j + ei[1][n])
            # if either inew or jnew is out of bound, it means no lattice to receive the particle.
            # then leave it blank.
            if inew < 0 or inew > (imax-1) or jnew < 0 or jnew > (jmax-1): continue
            ftmp[inew,jnew,n] = fi[i,j,n]

   # Boundary conditions based on bounce-back scheme
   for j in range(jmax):
      for i in range(imax):
         if (j > 0 and j < (jmax-1)) and (i > 0 and i < (imax-1)): continue
         for n in range(9):
            inew = int(i + ei[0][n])
            jnew = int(j + ei[1][n])
            # Following statement only sorts boundary lattices out.
            if inew < 0 or inew > (imax-1) or jnew < 0 or jnew > (jmax-1):
               inew = i
               jnew = j
               if n == 1: nnew = 3
               if n == 2: nnew = 4
               if n == 3: nnew = 1
               if n == 4: nnew = 2
               if n == 5: nnew = 7
               if n == 6: nnew = 8
               if n == 7: nnew = 5
               if n == 8: nnew = 6
               ftmp[inew,jnew,nnew] = ftmp[i,j,n]

   # moving lid
   j = jmax-1
   for i in range(imax):
      rhoTmp = 1.0 / (1.0 + v[i,j]) * (ftmp[i,j,0] + ftmp[i,j,1] + ftmp[i,j,3] + 2.0 * (ftmp[i,j,2] + ftmp[i,j,2] + ftmp[i,j,5]))
      ftmp[i,j,4] += 1.5 * rhoTmp * v[i,j]
      ftmp[i,j,7] += 0.5 * (ftmp[i,j,1] - ftmp[i,j,3]) - 1.0/6.0 * rhoTmp * v[i,j] - 0.5 * rhoTmp * u[i,j]
      ftmp[i,j,8] += 0.5 * (ftmp[i,j,3] - ftmp[i,j,1]) + 0.5 * rhoTmp * u[i,j] - 1.0/6.0 * rhoTmp * v[i,j]

   fi = ftmp


   ###
   ### compute macroscopic density and velocity components
   ###
   for j in range(jmax):
      for i in range(imax):
         rho[i,j] = np.sum(fi[i,j,:])
         # Skip updating velocities on boundary lattices in order to keep pre-specified BC values
         if i == 0 or i == (imax-1) or j == 0 or j == (jmax-1): continue
         u[i,j] = np.sum(c * ei[0] * fi[i,j,:]) / rho[i,j]
         v[i,j] = np.sum(c * ei[1] * fi[i,j,:]) / rho[i,j]


   ### Find equilibrium distribution function ###
   fieq = np.zeros((imax,jmax,9))
   for n in range(9):
       for j in range(jmax):
          for i in range(imax):
             Si = 3.0 * (ei[0][n] * u[i,j] + ei[1][n] * v[i,j]) / c
             Si += 4.5 * ((ei[0][n] * u[i,j] + ei[1][n] * v[i,j]) / c ) ** 2
             Si += -1.5 * (u[i,j] ** 2 + v[i,j] ** 2) / (c ** 2)
             Si = Si * wi[n]

             fieq[i,j,n] = rho[i,j] * (wi[n] + Si)



   # collision step
   fiNEW = fi + (fieq - fi) / tau
   fi    = fiNEW

   if (nIter % nIterWrite == 0):
      plotStreamLine(x, y, u, v, nIter)
      plotContour(x, y, u, v, nIter)

   print "|- nIter = %s" % nIter, ", t = %.6f" % t
   if (nIter >= maxIter): break




