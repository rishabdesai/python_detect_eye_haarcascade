"""
Linear Algebra is heavily used in AI and ML to analyse the properties of matrices and vectors.

Complex data can aften easily be represented in the form of a vector or a matrix.
Matrix: is a rectangle array of numbers arranged in rows and columns

"""

# import numpy as np  # import the library NumPy and name it as np
# a=np.array([11,22,33])  #Create one dimentional array (row vector)
# b=np.array([44,55,66])  #Create one dimentional array (row vector)
# c=np.add(a,b)  
# #print(c)


# x = np.array([[1,2,3],[4,5,6],[7,8,9]])
# y = np.array([[9,8,7],[6,5,4],[3,2,1]])
# print(x)
# print(x.ndim) #dimention of array
# print(x.size)  # number of elements in array
# print(x.shape) #order of matrix
# if x.shape ==y.shape:
#     #print(np.add(x,y)) # two matirces can be added only if they are of the smae order
#     print(x@y) #multiplication
#     print(np.linalg.matrix_rank(x))
# else:
#     print("order is not same")


# p=np.array([[1,2,3],[4,5,6],[7,8,88]])
# q=np.array([[1,2,3],[4,5,6],[4,5,6]])

# print(p.T) # print transpose matrix
# print(p.T.T) #print transpose of transpose matrix
# print(np.trace(p)) #print trace of matrix (sum of diagonals)
# print(np.linalg.det(p)) # print determinant 
# r = np.linalg.inv(p) # inverse
# print(r)
# print(p@r) # print product of matrix (product is an identity matrix, where all diabonal elements are 1 and rest are other than 0)


import numpy as np
import scipy as sp

a = np.array([[11,22,33],[44,55,66],[77,88,888]])
p,l,u = sp.linalg.lu(a)
print(p)
print(l)
print(u)
print(p@l@u)