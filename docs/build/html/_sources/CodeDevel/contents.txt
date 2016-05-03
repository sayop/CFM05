=================
 Code Instruction
=================

The present project is aimed to develop a computer program for solving a steady solution with Lattice Boltzmann Method (LBM). The code being used for answering all the question here is written with Python language. This program is to run with simple command::
 
  $ python main.py

Quick instruction for running the simulation
--------------------------------------------

The Python code used for this project can be cloned from *github.com* repository::

  $ git clone https://github.com/sayop/CFM05

You can also see the code directly by visiting the website: https://github.com/sayop/CFM05 If you clone the code, you will see the following set of files and directories::

  $ sayop@reynolds:~$ ls CFM05/
  docs  README.md  src

*docs* contains the document files set for the current project using *Sphinx* software. This *pdf* document is online available at: http://cfm05-gatech.readthedocs.org. The Python script for this simulation is stored in *src* folder.

Before running the simulation, you need to open the file named *input.in* using editor for example, VI on unix system::
 
  $ vi input.in

Then, you should be able to see the following set of simulation parameters::

  #grid dimension
  iDim            61
  jDim            61
  xmin            0
  xmax            60
  ymin            0
  ymax            60
  #boundary conditions
  uLeft           0.0
  vLeft           0.0
  uRight          0.0
  vRight          0.0
  uBottom         0.0
  vBottom         0.0
  uUp             10.0
  vUp             0.0
  # fluid kinematic properties
  nu              1.0
  pInit           10.0
  #simulation setup
  pCorr           1
  alpha           1.0
  pResidual       0.01
  maxIter         1
  Courant         0.5
  dtInit          0.0001
  Beta            0.5
  residualMin     0.00005
  #Post-Process
  nIterWrite      100

The parameter's name above will literally tell you what every single variables indicates in the simulation. For the post-processing as requested in this project, *nIterWrite* will write a solution plot and CSV file at speicifed interval of time integration number.
