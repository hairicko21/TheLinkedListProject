#NumPy: Third-party library for maniging arrays and performing
#numerical and mathematical operations in python.
import numpy

#The numpy array is a 'true array'
#it's an array with a FIXED SIZE, and we can't extend it.

array1 = numpy.array(['linux', 'windows', 'Mac OS X'])
print(array1[0])
print(array1[2])

#array1[3] = 'android'
#array1[4] = 'ios'
array1[2] = 'ios'
print (array1[2])


#print(array1[3])
#print(array1[4])
#use array when you know the preticular number wouldn't change
print(array1)

list1 = ['linux']