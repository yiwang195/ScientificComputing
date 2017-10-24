##NumpyDemo.py
##
## Description: shows the limitations of Python built-in data types in
##  executing some scientfic analyses.
##
## Source: https://campus.datacamp.com/courses/intro-to-python-for-data-science
##
## Fall 2016/ENV859

#Create a list of heights and weights
height = [1.73, 1.68, 1.17, 1.89, 1.79]
print height
weight = [65.4, 59.2, 63.6, 88.4, 68.7]
print weight

#Calculate BMI (wt/ht**2)
#bmi = weight/height ** 2
##-->Error! because you can do this to lists!
##-->The only way around this is to iterate through each item in the lists

#Solution: use NumPy!
import numpy as np
arrHeight = np.array(height)
print arrHeight
arrWeight = np.array(weight)
print arrWeight

arrBMI = arrWeight / arrHeight ** 2
print arrBMI