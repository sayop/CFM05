#!/usr/bin/env python
import matplotlib.pyplot as plt
import csv

dataFile1 = 'ghia_Re100.csv'
dataFile2 = '../../v-velocity_in_x.csv'

xList1 = []
xList2 = []
vVelList1 = []
vVelList2 = []

# read Ghia's data
with open(dataFile1, 'rb') as csvfile1:
   reader = csv.DictReader(csvfile1)
   for row in reader:
      xList1.append(float(row['x']))
      vVelList1.append(float(row['v-velocity']))


# read my simulation data
with open(dataFile2, 'rb') as csvfile2:
   reader = csv.DictReader(csvfile2)
   for row in reader:
      xList2.append(float(row['x']))
      vVelList2.append(float(row['v-velocity']))

MinX = min(xList2)
MaxX = max(xList2)
MinY = -0.27#min(vVelList2)
MaxY = 0.2#max(vVelList2)

p = plt.plot(xList1, vVelList1, 'ko', markersize=15, label="Ghia's data")
p = plt.plot(xList2, vVelList2, 'r-', label='40x40')
plt.setp(p, linewidth='3.0')

plt.axis([MinX,MaxX, MinY, MaxY])
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('x', fontsize=22)
plt.ylabel('V', fontsize=22)

plt.grid(True)
ax = plt.gca()
xlabels = plt.getp(ax, 'xticklabels')
ylabels = plt.getp(ax, 'yticklabels')
plt.setp(xlabels, fontsize=18)
plt.setp(ylabels, fontsize=18)
plt.legend(
          loc='lower left',
          borderpad=0.25,
          handletextpad=0.25,
          borderaxespad=0.25,
          labelspacing=0.0,
          handlelength=2.0,
          numpoints=1)
legendText = plt.gca().get_legend().get_texts()
plt.setp(legendText, fontsize=18)
legend = plt.gca().get_legend()
legend.draw_frame(False)
fig = plt.gcf()
fig.set_size_inches(7,6)
plt.tight_layout()
pltFile = 'v-velocity_in_x.png'
plt.savefig(pltFile, format='png')
plt.close()

print "%s DONE!!" % (pltFile)

