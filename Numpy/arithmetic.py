import numpy as np

#? Scaler Arithmetic

# a= np.array([1,2,3])
# print(a+1)
# [2 3 4]
# print(a-2)
# [-1  0  1]
# print(a * 3)
# [3 6 9]
# print(a / 4)
# [0.25 0.5  0.75]
# print(a ** 5)
# [  1  32 243]

#? Vectorized math function

# print(np.sqrt(a))
# [1.         1.41421356 1.73205081]

# a= np.array([1.01,2.5,3.99])
# print(np.round(a))
# # [1. 2. 4.]
# print(np.floor(a))
# # [1. 2. 3.]
# print(np.ceil(a))
# # [2. 3. 4.]

# print(np.pi)
# 3.141592653589793

# rad = np.array([1,2,3])
# print(np.pi * rad ** 2)
# [ 3.14159265 12.56637061 28.27433388]

#? Element-wise areithmetic

# a = np.array([1,2,3])
# b = np.array([4,5,6])
# print(a+b)
# [5 7 9]
# print(a-b)
# [-3 -3 -3]
# print(a*b)
# [ 4 10 18]
# print(a/b)
# [0.25 0.4  0.5 ]
# print(a ** b)
# [  1  32 729]

#? Comparison operators

score = np.array([91, 55, 100, 73, 82, 64])

# print(score == 100)
#[False False  True False False False]

# print(score >= 60)
# [ True False  True  True  True  True]

# print(score <= 60)
# [False  True False False False False]

score[score < 60] = 0
print(score)
# [ 91   0 100  73  82  64]
