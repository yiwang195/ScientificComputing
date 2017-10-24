# B_NumpyArraysFromLists.py
#
# Exercises on creating and manipulating NumPy arrays from lists.
#
# Env859, Fall 2016
# John.Fay@duke.edu

# Import modules
import sys, os
import numpy as np

## 1. Creating numpy arrays from a list ------------------------------
# Lists can be converted into a NumPy array easily
# **if all elements are of the same data type**
height = [1.73, 1.68, 1.17, 1.89, 1.79]
np_height = np.array(height)
print np_height

## EXERCISE 1 *********************************************************
##  create an array from the weight list 
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
np_weight = np.array(weight)
print np_weight
##********************************************************************

# When lists contain > 1 data type, the elements in the resulting 
# array are 'coerced' to the least common demoninator (often strings)
oddList = [202, "John", False]
np_odd = np.array(oddList)
print np_odd
print np_odd.dtype  #Prints the data type of the array

np_odd2 = np.array([False, 1, 200])
print np_odd2
print np_odd2.dtype #Booleans and ints default to int32

## EXERCISE 2 ******************************************************
## In the np_odd2 array above, what values does False get assigned?
## What value would True be?
##
## Change last item from 200 to 200.0;
##  What data type is the resulting array?
##********************************************************************


