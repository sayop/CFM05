#!/usr/bin/env python
import sys
import numpy as np
import time
sys.path.append('./functions')
from variables import *
from IO import *
from domain import *
from init import *
from timeIntegrate import *

# read input parameters from input.in
inputDict = readInput()

# create domain
createDomain(inputDict)

# Initialize flow variables
initSimulationVars(inputDict)

# main loop for time integration
timeIntegrate(inputDict)
