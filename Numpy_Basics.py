import math
from sys import getsizeof

import numpy as np
import random as rd

my_array = np.array([1,2,3,4,5])*2
print(my_array)
print(type(my_array))

my_array2 = np.array([[1,2,3,4,5],
                       [1,2,3,4,5]
                      ,[1,2,3,4,5]])*2
print(my_array2)
print(type(my_array2))
print(my_array2.ndim)

my_array3 = np.array([[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],
                      [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]],
                      [[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]])*2

print(my_array3)
print(type(my_array3))
print(my_array3.ndim)
print(my_array3.shape)

#indexing

#normal python
print(my_array3[0][0][0]) #first list second list third list item one
#numpy one
print(my_array3[0,0,0]) #you just use a comma instead of three brakets
print('-----------------------------------------------------------------------')

word = ""
itnum = iter(range(3))
while True:
    try:
     i  = next(itnum)
     number = my_array3[0,i,i+1]
     word = word + str(number)
    except StopIteration:
        break
print(word)
#same thing
for i in range(3):
    print(my_array3[i,i,i+1], end="")

print("\n------------------------------------------------------------------------------------------")
my_array4 = np.array([[["A"],["B"],["C"],
                       ["D"],["E"],["F"],
                       ["G"],["H"],["I"],
                       ["J"],["K"],["L"],
                       ["M"],["N"],["O"],
                       ["P"],["Q"],["R"],
                       ["S"],["T"],["U"],
                       ["V"],["W"],["X"],
                       ["Y"],["Z"]]])

word = ""
print(word)
print(type(word))
print(getsizeof(word))
for i in range(3):
    random = rd.randint(0,25)
    alpha = my_array4[0,random]
    alpha = alpha[0]
    word+=alpha

print(word, end="")

#slicing array[start:end:step]
print('-----------------------------------------------------------------------')

print(my_array3[1:3,0:2,0:2])

#array square root

print(np.sqrt(my_array3))
print(np.round(my_array3))

my_array6 = np.array([5,10,20]) **2
result = np.trunc((my_array6 * np.pi) * 10)/10
print()
print(result)


#bool

print(result == 78.5)

array = np.array([1,2,3,4,5])
array2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
print(array.shape)
print(array2.shape)
array = array + array2
print(array)

#aggregate functions
array = np.array([[1,2,4,4,5],
                  [1,2,4,4,50],
                  [1,2,4,4,50]])
print(np.sum(array))
print(np.mean(array))
print(np.median(array))
print(np.std(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))
print(np.argmax(array))
print("axis",np.sum(array, axis=1))
#idk
number = np.array([4,7,13,16])
print(np.mean(number))
sum = np.array([6,3,-3,-6])**2
sum = np.sum(sum)
sum = sum/4
print(np.sqrt(sum))

diaviation = np.array([3,7,11,15,19])
mean = np.mean(diaviation)
distance = diaviation - mean
squared = distance**2
sum_squared_distance = np.sum(squared)
squared_distance = sum_squared_distance/5
print(np.sqrt(squared_distance))

print(math.sqrt(21))


my_array7 = np.array([[1,2,3,4,5],
                      [1,2,3,4,5],
                      [1,2,3,4,5],])

num = my_array7[(my_array7 > 1 )]
print(num)

#randomrandint in numpy
random = np.random.default_rng(seed=0)
print(random.integers(1,100,size=(3,2)))
