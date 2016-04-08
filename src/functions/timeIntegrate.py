import numpy as np
from solutionMethod import *
from variables import *
import time

def timeIntegrate(inputDict):
   tStart  = 0.0
   imax    = int(inputDict['iDim'])
   jmax    = int(inputDict['jDim'])
   maxIter = int(inputDict['maxIter'])

   # start to count time for calculting computation performance
   start = time.clock()

   # Non-dimensionalize flow and domain variables
   nondimensionalize(inputDict)

   # setup streaming velocity vector e_i
   setupLBMparameters()

   # Set initial distribution function at equilibrium
   findEquilibriumDistributionFunction(imax,jmax)

   # Initialize distribution function with equilibrium distribution function
   LBM.fi = LBM.fieq

   #
   # Time Marching:
   #
   print '=============================================='
   print '# Time integration starts at t = %s' % tStart
   print '=============================================='
   t = tStart
   nIter = 0

   while True:
      nIter += 1
      t += timeVars.dt

      # Streaming step
      streaming(imax,jmax)

      # compute macroscopic density and velocity components
      updateFlowVarsFromDistributionFuction(imax,jmax)
 
      # compute fi_eq
      findEquilibriumDistributionFunction(imax,jmax)

      # collision step
      collision(imax,jmax)

      print flowVars.rho

      print "|- nIter = %s" % nIter, ", t = %.6f" % t
      if (nIter >= maxIter): break
