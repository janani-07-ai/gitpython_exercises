# write a program to perform add,sub,mult,div on two given matrices in python
import numpy as np
x= np.array([ [2,7,3],[4,5,6],[7,8,9]])
y= np.array([ [5,8,1],[6,7,3],[4,5,9]])
print("the values of x :")
print(x)
print("the values of y :")
print(y)
print("the addition of x and y:\n",np.add(x,y))
# subtraction
x= np.array([ [2,7,3],[4,5,6],[7,8,9]])
y= np.array([ [5,8,1],[6,7,3],[4,5,9]])
print("the values of x :")
print(x)
print("the values of y :")
print(y)
print("the subtraction of x and y:\n",np.subtract(x,y))

# multiplication
x= np.array([ [2,7,3],[4,5,6],[7,8,9]])
y= np.array([ [5,8,1],[6,7,3],[4,5,9]])
print("the values of x :")
print(x)
print("the values of y :")
print(y)
print("the multiplication of x and y:\n",np.multiply(x,y))

# division

x= np.array([ [2,7,3],[4,5,6],[7,8,9]])
y= np.array([ [5,8,1],[6,7,3],[4,5,9]])
print("the values of x :")
print(x)
print("the values of y :")
print(y)
print("the division of x and y:\n",np.divide(x,y))
