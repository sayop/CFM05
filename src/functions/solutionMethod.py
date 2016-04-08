from variables import *
import numpy as np

def nondimensionalize(inputDict):
   Lref = domainVars.Lref
   domainVars.x = domainVars.x / Lref
   domainVars.y = domainVars.y / Lref
   domainVars.dx = domainVars.dx / Lref
   domainVars.dy = domainVars.dy / Lref

   Uref = flowVars.Uref
   flowVars.u = flowVars.u / Uref
   flowVars.v = flowVars.v / Uref

def setupLBMparameters():

   # Setup streaming velocity unit vector: e_i
   # x component of e_i vector
   LBM.ei[0] = np.zeros(9)
   # y component of e_i vector
   LBM.ei[1] = np.zeros(9)

   LBM.ei[0][1] = 1
   LBM.ei[0][3] = -1
   LBM.ei[0][5] = 1
   LBM.ei[0][6] = -1
   LBM.ei[0][7] = -1
   LBM.ei[0][8] = 1

   LBM.ei[1][2] = 1
   LBM.ei[1][4] = -1
   LBM.ei[1][5] = 1
   LBM.ei[1][6] = 1
   LBM.ei[1][7] = -1
   LBM.ei[1][8] = -1

   # Setup weight coefficient, w_i
   LBM.wi = np.zeros(9) 

   LBM.wi[0] = 4.0 / 9.0
   LBM.wi[1] = 1.0 / 9.0
   LBM.wi[2] = 1.0 / 9.0
   LBM.wi[3] = 1.0 / 9.0
   LBM.wi[4] = 1.0 / 9.0
   LBM.wi[5] = 1.0 / 36.0
   LBM.wi[6] = 1.0 / 36.0
   LBM.wi[7] = 1.0 / 36.0
   LBM.wi[8] = 1.0 / 36.0

   # Setup streaming speed c = dx/dt
   LBM.c = domainVars.dx / timeVars.dt
   print "LBM streaming speed, c = ", LBM.c

   # Setup speed of sound, Cs
   LBM.cs = LBM.c / np.sqrt(3.0)
   print "LBM speed of sound, Cs = ", LBM.cs

   # Setup relaxation time, tau
   LBM.tau = 0.5 * (6.0 * flowVars.nu / (LBM.c ** 2 * timeVars.dt) + 1.0)
   print "LBM relaxation time, tau = ", LBM.tau

def findEquilibriumDistributionFunction(imax,jmax):
   LBM.fieq = np.zeros((imax,jmax,9))
   for n in range(9):
       for j in range(jmax):
          for i in range(imax):
             Si = 3.0 * (LBM.ei[0][n] * flowVars.u[i,j] + LBM.ei[1][n] * flowVars.v[i,j]) / LBM.c
             Si += 4.5 * ((LBM.ei[0][n] * flowVars.u[i,j] + LBM.ei[1][n] * flowVars.v[i,j]) / LBM.c ) ** 2
             Si += -1.5 * (flowVars.u[i,j] ** 2 + flowVars.v[i,j] ** 2) / (LBM.c ** 2)
             Si = Si * LBM.wi[n]

             LBM.fieq[i,j][n] = flowVars.rho[i,j] * (LBM.wi[n] + Si)

   
def updateFlowVarsFromDistributionFuction(imax,jmax):

   for j in range(jmax):
      for i in range(imax):
         flowVars.rho[i,j] = np.sum(LBM.fi[i,j])
         flowVars.u[i,j] = np.sum(LBM.c * LBM.ei[0] * LBM.fi[i,j])
         flowVars.v[i,j] = np.sum(LBM.c * LBM.ei[1] * LBM.fi[i,j])

def streaming(imax,jmax):

   ftmp = np.zeros((imax,jmax,9))

   for j in range(jmax):
      for i in range(imax):
         for n in range(9):
            inew = int(i + LBM.ei[0][n])
            jnew = int(j + LBM.ei[1][n])
            nnew = n
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
            ftmp[inew,jnew,nnew] = LBM.fi[i,j][n]

   LBM.fi = ftmp 
