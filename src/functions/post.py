import numpy as np
import matplotlib.pyplot as plt
import csv

def plotContour(x,y,U,V,nIter):
   from matplotlib import mlab, cm
   cmap = cm.PRGn

   pltFile = 'contour_vel_%5.5d.png' % int(nIter)
   x = np.asarray(x)
   y = np.asarray(y)
   #U = np.swapaxes(U,1,0)
   #V = np.swapaxes(V,1,0)
   #xi, yi = np.meshgrid(x, y)
   #zi = np.swapaxes(phi,1,0)

   Umag = np.sqrt( U ** 2 + V ** 2 )
   Umag = np.swapaxes(Umag,0,-1)
   phiMin = Umag.min()
   phiMax = Umag.max()
   #nLevels = 10
   #dPhi = (phiMax - phiMin) / nLevels
   #levels = np.arange(phiMin, phiMax*1.001, dPhi)

   #plt.contour(xi,yi,zi,levels)
   plt.imshow(Umag, vmin=phiMin, vmax=phiMax, extent=[x.min(), x.max(), y.min(), y.max()])
   plt.colorbar()

   plt.xscale('linear')
   plt.yscale('linear')
   plt.xlabel('x', fontsize=18)
   plt.ylabel('y', fontsize=18)
   #plt.grid(True)
   ax = plt.gca()
   xlabels = plt.getp(ax, 'xticklabels')
   ylabels = plt.getp(ax, 'yticklabels')
   plt.setp(xlabels, fontsize=15)
   plt.setp(ylabels, fontsize=15)

   fig = plt.gcf()
   fig.set_size_inches(6,5)
   plt.tight_layout()
   plt.savefig(pltFile, format='png')
   plt.close()

   print "%s DONE!!" % (pltFile)
   plt.show()

def plotStreamLine(x,y,U,V,nIter):
   pltFile = 'streamLine_%5.5d.png' % int(nIter)
   x = np.asarray(x)
   y = np.asarray(y)
   U = np.swapaxes(U,1,0)
   V = np.swapaxes(V,1,0)

   strm = plt.streamplot(x,y,U,V, color='k', density=1, linewidth=1)

   plt.axis([x.min(), x.max(), y.min(), y.max()])
   plt.xscale('linear')
   plt.yscale('linear')
   plt.xlabel('x [m]', fontsize=18)
   plt.ylabel('y [m]', fontsize=18)
   plt.grid(True)
   ax = plt.gca()
   xlabels = plt.getp(ax, 'xticklabels')
   ylabels = plt.getp(ax, 'yticklabels')
   plt.setp(xlabels, fontsize=10)
   plt.setp(ylabels, fontsize=10)

   fig = plt.gcf()
   fig.set_size_inches(6,5)
   plt.tight_layout()
   plt.savefig(pltFile, format='png')
   plt.close()

   print "%s DONE!!" % (pltFile)
   plt.show()

def traceCenterLineData(direction, phi, csvFile):
   from variables import *
   import csv

   x = domainVars.x
   y = domainVars.y
   imax = len(x)
   jmax = len(y)

   if direction == 'x':
      yCenter = 0.5 * (min(y) + max(y))
      # find j index for yCenter
      for j in range(jmax-1):
         if yCenter >= y[j] and yCenter < y[j+1]:
            jL = j
            distL = yCenter - y[j]
            jR = j+1
            distR = y[j+1] - yCenter
      # loop over v-velocity in x-direction along the geometrically horizontal centerline
      data = []
      for i in range(imax):
         dataL = phi[i,jL]
         dataR = phi[i,jR]
         target = dataL + (dataR - dataL) * distL / (distL + distR)
         data.append(target)

   elif direction == 'y':
      xCenter = 0.5 * (min(x) + max(x))
      # find i index for xCenter
      for i in range(imax-1):
         if xCenter >= x[i] and xCenter < x[i+1]:
            iL = i
            distL = xCenter - x[i]
            iR = i+1
            distR = x[i+1] - xCenter
      # loop over u-velocity in y-direction along the geometrically vertical centerline
      data = []
      for j in range(jmax):
         dataL = phi[iL,j]
         dataR = phi[iR,j]
         target = dataL + (dataR - dataL) * distL / (distL + distR)
         data.append(target)

   c = csv.writer(open(csvFile, "wb"))
   if direction == 'x':
      c.writerow(["x","v-velocity"])
      for i in range(imax):
         c.writerow([x[i], data[i]])
   elif direction == 'y':
      c.writerow(["y","u-velocity"])
      for j in range(jmax):
         c.writerow([y[j], data[j]])

   print "%s DONE!!" % (csvFile)

def logResidual(res, csvFile):
   import csv
   nData = len(res)
   c = csv.writer(open(csvFile, "wb"))
   c.writerow(["nIter","residual"])
   for n in range(nData):
      c.writerow([n+1, res[n]])
   print "%s DONE!!" % (csvFile)
