from variables import *

def readInput():
   print '# Reading input file...'

   inputDict = {}
   with open("inputs.in") as f:
      for line in f:
         li = line.strip()
         if li.startswith("#"): continue
         (key, val) = line.split()
         inputDict[key] = val

   return inputDict
