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
