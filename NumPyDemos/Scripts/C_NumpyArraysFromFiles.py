# NumpyArraysFromFiles.py
#
# Exercises on creating NumPy arrays from text files.
#
# Note: Numpy works best when all the values in a file are numeric.
#       If you want to import files with mixed data types, you should
#       use Pandas, which we will cover next. 
#
# Env859, Fall 2016
# John.Fay@duke.edu

# Import modules
import sys, os
import numpy as np

## Reading data in from CSV files - Part 1 (easy)
# Here we'll read in a CSV file from the EPA's EnviroAtlas dataset
# stored in the W:/859_datafolder. The file we will look at is
# ImpairedWater.csv. Open the file in NotePad++ to see what the it
# looks like. 

#Get the file name
csvFileName = "W:\\859_data\NATIONAL_METRICS_JULY2015_CSV\ImpairedWater.csv"

#Use the genfromtxt function to read in the data; view the syntaxt of the function
help(np.genfromtxt)
#The default delimiter is a space, so we need to change that to a comma
#Our CSV file has one header row, so we also need to set that to skip that
np_impaired = np.genfromtxt(csvFileName,delimiter=",",skip_header=1)

##---> What type is the resulting array? 

#Use the shape function to see how many rows and columns are returned
#You should have 83035 rows and 14 columns
print np_impaired.shape

#View the first row in the array
print np_impaired[0]

## Reading data in from CSV files - Part 1 (less easy)
# Now we'll open the sara.txt file. This file has a section of comments
# at the start, so we'll have to filter those out here.

# Again, get the file name
csvFileName = "W:\\859_data\\sara.txt"

# Convert using the genfromtxt function, but set the comments argument
np_sara = np.genfromtxt(csvFileName,delimiter="\t",skip_header=1,comments='#')

# Check that it imported ok by looking at the first record
print np_sara[0]

## Uh-oh! What happened? Well, turns out skip_header only skips rows at the
## the beggining of the file. We'll have to improvise.Not perfect, but
## this give you an idea of some gotchas when importing data into numpy...

np_sara2 = np_sara = np.genfromtxt(csvFileName,delimiter="\t",skiprows=17)

##---> Why 17 in the above line?
##---> What is the data type of the np_sara2 array?
##---> How many rows and columns were imported?
##---> What are the values of the 75 row of data? 