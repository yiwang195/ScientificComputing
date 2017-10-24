#ARGOSReAnalysis.py
#
# Description: Revisits the ARGOS scripting exercise we did, but doing the
#  analysis using Pandas which makes it much easier...
#
# Env859, Fall 2016
# John.Fay@duke.edu

# Import modules
import sys, os
import numpy as np
import pandas as pd

# Set user inputs (these can be switched to user inputs
date = "7/3/2003"
lc_filters = "1;2;3"

# Set relative paths
scriptDir = os.path.dirname(sys.argv[0])
rootDir = os.path.dirname(scriptDir)
dataDir = os.path.join(rootDir,"Data")
scratchDir = os.path.join(rootDir,"Scratch")

## Use the Pandas loadtxt function to read in data the sara.txt file-----
# set the comment parameter to '#' to skip lines beginning with '#'
# set to use tabs as the field delimiter
# the result is a pandas data frame
inputFN = os.path.join(dataDir,"sara.txt")              
DF = pd.read_csv(inputFN,comment='#',delimiter="\t")

## Display formation about the data frame object
print type(DF)      #Show the data type of the data frame
print DF.shape      #Prints the shape (rows, columns) of the frame
print DF.columns    #List the columns that were imported
print DF.dtypes     #List the columns and their data types
print DF.head(3)    #Show the first 3 records

## Change the data type of the utc column to a data format
# ...to figure out how to do this, I Googled "pandas convert columns to date"
#    and then gave it a try...
#DF["utc"] = pd.to_datetime(DF["utc"])

## Use Pandas return a data frame of select columns
keeper_columns = ['uid','lc','lat1','lon1','utc']
keeperDF = DF[keeper_columns]
print keeperDF.head(3)

## Use Pandas to return a data frame of select rows
#First, convert the multi-input string ot a list of value
lcList = lc_filters.split(";")
#We can use the 'isin' method to select records where the location class is in the list (1,2,3)
DF2 = DF[DF['lc'].isin(lcList)]
#Now we select records that match the date
DF3 = DF2[DF2['utc'].str.contains(date)]

## Finally we report the results
print "----------------------------------------------"
print "On %s, Sara was obsserved at: " %date
for x in range(0,len(DF3)):
    print "  Lat: %2.4f; Long: %2.4f" %(DF3.iloc[x]['lat1'],DF3.iloc[x]['lon1'])
