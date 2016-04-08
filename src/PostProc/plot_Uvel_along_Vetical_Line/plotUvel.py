#!/usr/bin/env python
import matplotlib.pyplot as plt
import csv

dataFile1 = 'ghia_Re100.csv'
dataFile2 = '../../u-velocity_in_y.csv'

yList1 = []
yList2 = []
uVelList1 = []
uVelList2 = []

# read Ghia's data
with open(dataFile1, 'rb') as csvfile1:
   reader = csv.DictReader(csvfile1)
   for row in reader:
      yList1.append(float(row['y']))
      uVelList1.append(float(row['u-velocity']))


# read my simulation data
with open(dataFile2, 'rb') as csvfile2:
   reader = csv.DictReader(csvfile2)
   for row in reader:
      yList2.append(float(row['y']))
      uVelList2.append(float(row['u-velocity']))

MinY = min(yList2)
MaxY = max(yList2)
MinX = -0.25#min(uVelList2)
MaxX = 1.0#max(uVelList2)

p = plt.plot(uVelList1,yList1, 'ko', markersize=15, label="Ghia's data")
p = plt.plot(uVelList2,yList2, 'r-', label='40x40')
plt.setp(p, linewidth='3.0')

plt.axis([MinX,MaxX, MinY, MaxY])
plt.xscale('linear')
plt.yscale('linear')
plt.xlabel('U', fontsize=22)
plt.ylabel('y', fontsize=22)

plt.grid(True)
ax = plt.gca()
xlabels = plt.getp(ax, 'xticklabels')
ylabels = plt.getp(ax, 'yticklabels')
plt.setp(xlabels, fontsize=18)
plt.setp(ylabels, fontsize=18)
plt.legend(
          loc='lower right',
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
fig.set_size_inches(6,6)
plt.tight_layout()
pltFile = 'u-velocity_in_y.png'
plt.savefig(pltFile, format='png')
plt.close()

print "%s DONE!!" % (pltFile)

