import numpy as np
from solutionMethod import *
from variables import *
from post import *
import time

def timeIntegrate(inputDict):
   tStart  = 0.0
   imax    = int(inputDict['iDim'])
   jmax    = int(inputDict['jDim'])
   maxIter = int(inputDict['maxIter'])
   nIterWrite  = int(inputDict['nIterWrite'])

   # start to count time for calculting computation performance
   start = time.clock()

   # Non-dimensionalize flow and domain variables
   #nondimensionalize(inputDict)

   # setup streaming velocity vector e_i
   setupLBMparameters()

   # Set initial distribution function at equilibrium
   #findEquilibriumDistributionFunction(imax,jmax)

   # Initialize distribution function with equilibrium distribution function
   #LBM.fi = LBM.fieq
   LBM.fi = np.ones((imax,jmax,9))

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


      # compute fi_eq
      findEquilibriumDistributionFunction(imax,jmax)


      # collision step
      LBM.fi += (LBM.fieq - LBM.fi) / LBM.tau



      # compute macroscopic density and velocity components
      updateFlowVarsFromDistributionFuction(imax,jmax)

      if (nIter % nIterWrite == 0):
         #dimensionalize(inputDict)
         plotStreamLine(domainVars.x, domainVars.y, flowVars.u, flowVars.v, nIter)
         plotContour(domainVars.x, domainVars.y, flowVars.u, flowVars.v, nIter)
         #nondimensionalize(inputDict)

 
      print "|- nIter = %s" % nIter, ", t = %.6f" % t
      if (nIter >= maxIter): break

   #
   # time elapsed:
   elapsedTime = (time.clock() - start)
   print "## Elapsed time: ", elapsedTime

   # Dimensionalize flow and domain variables
   #dimensionalize(inputDict)

   # plot streamline of velocity
   plotStreamLine(domainVars.x, domainVars.y, flowVars.u, flowVars.v, nIter)

   # trace center-line data to be compared to the Ghia's paper data
   #nondimensionalize(inputDict)
   traceCenterLineData('x', flowVars.v, 'v-velocity_in_x.csv')
   traceCenterLineData('y', flowVars.u, 'u-velocity_in_y.csv')
   #dimensionalize(inputDict)

