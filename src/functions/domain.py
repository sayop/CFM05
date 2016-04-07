import numpy as np
from variables import domainVars

def createDomain(inputDict):
   print '# Creating one-dimensional domain...'
   imax = int(inputDict['iDim'])
   jmax = int(inputDict['jDim'])
   xmin = float(inputDict['xmin'])
   xmax = float(inputDict['xmax'])
   ymin = float(inputDict['ymin'])
   ymax = float(inputDict['ymax'])
   x = np.zeros(imax)
   y = np.zeros(jmax)

   dx = (xmax - xmin) / (imax - 1)
   dy = (ymax - ymin) / (jmax - 1)
   for i in range(imax):
      x[i] = xmin + dx * i

   for j in range(jmax):
      y[j] = ymin + dy * j

   domainVars.x = x
   domainVars.y = y
   domainVars.dx = dx
   domainVars.dy = dy
   domainVars.Lref = xmax - xmin
   return
