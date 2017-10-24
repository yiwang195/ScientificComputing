# D_NumpySubsetting.py
#
# Exercises on subsetting NumPy arrays.
#
# Env859, Fall 2016
# John.Fay@duke.edu

# Import modules
import sys, os
import numpy as np

# Create the sample array
height = [1.73, 1.68, 1.17, 1.89, 1.79]
np_height = np.array(height)

## 1. Extracting values from the array
# First we create a boolean array, that is an array of true/false
# values where true values correspond to a criteria.
np_filter = np_height < 1.7
print np_filter.dtype
print np_filter

# Then we can apply that boolean filter to the original array
# which will result in only the 'true' values being kept.
np_shorties = np_height[np_filter]
print np_shorties

# Or we can combine these into one step
np_shorties2 = np_height[np_height < 1.7]
print np_shorties2

## 2. Extracting data from multi-dimensional arrays
# Let's re-import the impaired water data into a 2d array
# and examine how to select items from this
csvFileName = "W:\\859_data\NATIONAL_METRICS_JULY2015_CSV\ImpairedWater.csv"
npWater = np.genfromtxt(csvFileName,delimiter=",",skip_header=1)
print npWater.shape

# We saw how to get a single row by its index; this returns all columns for
# the 21st row of data
print npWater[20]

# We can get the value of the first 3 columns of the 21st row this way
print npWater[20,0:3]

# Or we can select all rows, but just select columns, here get the 13th column
npTotImpLen = npWater[:,12]
print npTotImpLen.shape

# We can calculate the mean of all these columns
print npTotImpLen.mean()

# We can, as above select rows that meet a criteria, here TotImpLen > 0.1
npImpaired = npWater[npWater[:,12] > 50]
print npImpaired.shape
print npImpaired.max()

## Are stream density and total impaired length corelated
npStreamDensity = npWater[:,7]
print np.corrcoef(npStreamDensity, npTotImpLen)