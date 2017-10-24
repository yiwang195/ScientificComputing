#Imports
import sys, os, arcpy
import numpy as np
import scipy.ndimage as nd
from matplotlib import pyplot as plt

#Paths
scriptDir = os.path.dirname(sys.argv[0])
rootDir = os.path.dirname(scriptDir)
dataDir = os.path.join(rootDir,"Data","PilotMtn.gdb")
scratchDir = os.path.join(rootDir,"Scratch")

#Data
DEM = os.path.join(dataDir,"elev_cm")

#Conver to numpy array
r = arcpy.RasterToNumPyArray(DEM,"",200,200,0)

fig = plt.figure(figsize=(10,10))

for i in xrange(25):
    size = (i+1) * 3
    print "running {}".format(size)
    med = nd.median_filter(r, size)
    a = fig.add_subplot(5, 5,i+1)
    plt.imshow(med, interpolation='nearest')
    a.set_title('{}x{}'.format(size, size))
    plt.axis('off')
    plt.subplots_adjust(hspace = 0.1)
    prev = med
    
plt.savefig("btm-scale-compare.png", bbox_inches='tight')

