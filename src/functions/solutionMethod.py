from variables import flowVars, domainVars, LBM
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

   LBM.ei[0][1] = 1.0
   LBM.ei[0][3] = -1.0
   LBM.ei[0][5] = 1.0
   LBM.ei[0][6] = -1.0
   LBM.ei[0][7] = -1.0
   LBM.ei[0][8] = 1.0

   LBM.ei[1][2] = 1.0
   LBM.ei[1][4] = -1.0
   LBM.ei[1][5] = 1.0
   LBM.ei[1][6] = 1.0
   LBM.ei[1][7] = -1.0
   LBM.ei[1][8] = -1.0

   # Setup weight coefficient, w_i
   LBM.wi = np.zeros(9) 

   LBM.wi[0] = 0.0
   LBM.wi[1] = 1.0 / 9.0
   LBM.wi[2] = 1.0 / 9.0
   LBM.wi[3] = 1.0 / 9.0
   LBM.wi[4] = 1.0 / 9.0
   LBM.wi[5] = 1.0 / 36.0
   LBM.wi[6] = 1.0 / 36.0
   LBM.wi[7] = 1.0 / 36.0
   LBM.wi[8] = 1.0 / 36.0

def findEquilibriumDistributionFunction(imax,jmax):
   LBM.fieq = np.zeros((9,imax,jmax))
   for i in range(9):
      LBM.fieq[
