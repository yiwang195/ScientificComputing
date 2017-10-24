# NumpyArraysFromArcGIS.py
#
# Demonstrates how arrays can be created from feature classes,
#  table, and rasters
#
# Env859, Fall 2016
# John.Fay@duke.edu

# Import modules
import sys, os, arcpy
import numpy as np

# Set relative paths
scriptDir = os.path.dirname(sys.argv[0])
rootDir = os.path.dirname(scriptDir)
dataDir = os.path.join(rootDir,"Data")
scratchDir = os.path.join(rootDir,"Scratch")

# Path to the HUC12 feature class and elev_cm raster
huc12_fc = os.path.join(dataDir,"HUC12.shp")
elev_raster = os.path.join(dataDir,"PilotMtn.gdb","elev_cm")

## Convert HUC12 feature class to a NumPy array----------------------
# See http://desktop.arcgis.com/en/arcmap/latest/analyze/arcpy-data-access/featureclasstonumpyarray.htm

# First, create a list of the fields you want; we'll just pull in three. Using "*" imports all fields. 
fields = ["HUC_8","HUC_12","ACRES"]

# Use the FeatureClassToNumpyArray command (da module) to import all into an array
huc12_np = arcpy.da.FeatureClassToNumPyArray(huc12_fc,fields)

# Show properties of the returned NumPy array
print huc12_np.shape
print huc12_np.dtype
print huc12_np[0]

## Note the shape has just 210 rows and "no" columns. That is because the huc12_np is
## a "record array" which is slightly different than the "structured array" we were using
## up to this point. See the Numpy documentation for full details, but the relevant difference
## between the two here is that items in a record array can be retrieved by attribute vs index.
## Docs: https://docs.scipy.org/doc/numpy/user/basics.rec.html
## (more on this later, when we discuss manipulating arrays)

# Print the HUC_8 value of the first record
print huc12_np[0]["HUC_8"]

## Convert the raster to a numpy array 
elev_np = arcpy.RasterToNumPyArray(elev_raster)
print elev_np.shape

#What is the mean elevation of all pixels?
print elev_np.mean()

#Convert data from cm to feet
elevft_np = elev_np * 0.0328084

#Write back to a raster using NumPyArrayToRaster (see documentation)
outRaster = os.path.join(scratchDir,"elev_ft.img")
d = arcpy.Describe(elev_raster)     #We need some info from the source raster
sr = d.SpatialReference             #The spatial reference
ext = d.Extent                      #The extent
cellSize = d.meanCellHeight         #The cell size
ll = arcpy.Point(ext.XMin,ext.YMin) #Create a point at the lower left corner
#With all that info collected, we can write out our array
elevft_raster = arcpy.NumPyArrayToRaster(elevft_np,ll,cellSize,cellSize)
elevft_raster.save(outRaster)
#Don't forget to define its projection! 
elevft_raster = arcpy.DefineProjection_management(elevft_raster,sr)