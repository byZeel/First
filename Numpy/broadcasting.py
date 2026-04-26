import numpy as np

#! Broadcasting allows Numpy to perform operation on arrays
#! With different shape by virtually expanding dimensions
#! so thet match the larger array's shape

#! The dimensions have the same size.
#! Or
#! One of the dimension has a size of 1. to do arithmetic
#todo so (1,4)*(4,1),(2,4)*(2,4) is possible but (2,4)*(4,2),(2,4)(4,4) not

# a= np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
# b= np.array([[1,1],[2,2],[3,3],[4,4]])

# print(a.shape)
# print(b.shape)

# print(a * b)

# a = np.array([[1,2,3,4,5,6,7,8,9,10]])
# b = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

print(a * b)
