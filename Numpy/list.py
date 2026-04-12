import numpy as np # type: ignore

# print(np.__version__)
# 2.4.2

# a=[1,2,3]
# b=a*2
# b[0]=99
# print(a)
# [1, 2, 3]
# print(b)
# [99, 2, 3, 1, 2, 3]

# list = [1,2,3,4]
# list=2*list
# [1, 2, 3, 4, 1, 2, 3, 4]
# print(list)

# list = np.array([1,2,3,4])
# list=2*list
# print(list)
# [2 4 6 8]
# print(type(list))
# <class 'numpy.ndarray'>  (which means n demention array)

# array=np.array(['A'])
# print(array.ndim)
# 1
# array=np.array('A')
# print(array.ndim)
# 0
# array=np.array(['A','B','C'])
# print(array.ndim)
# 1
# array=np.array([['A','B','C'],
#                 ['D','E','F'],
#                 ['G','H','I']])
# print(array.ndim)
# 3
# array=np.array([['A','B','C'],['D','E','F'],['G','H','I'],
#                 ['J','K','L'],['M','N','O'],['P','Q','R'],
#                 ['S','T','U'],['V','W','X'],['Y','Z',' ']])
# print(array)
# [['A' 'B' 'C']
#  ['D' 'E' 'F']
#  ['G' 'H' 'I']
#  ['J' 'K' 'L']
#  ['M' 'N' 'O']
#  ['P' 'Q' 'R']
#  ['S' 'T' 'U']
#  ['V' 'W' 'X']
#  ['Y' 'Z' ' ']]
# array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
#                 [['J','K','L'],['M','N','O'],['P','Q','R']],
#                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
# print(array.ndim)
# [[['A' 'B' 'C']
#   ['D' 'E' 'F']
#   ['G' 'H' 'I']]

#  [['J' 'K' 'L']
#   ['M' 'N' 'O']
#   ['P' 'Q' 'R']]

#  [['S' 'T' 'U']
#   ['V' 'W' 'X']
#   ['Y' 'Z' ' ']]]

# print(array[0,2,1]+array[0,1,1]+array[2,2,0]+" "+array[2,2,1]+array[0,1,1]+array[0,1,1]+array[1,0,2])
# HEY ZEEL
# print(array[0,2,1]+array[0,1,1]+array[2,2,0]," ",array[2,2,1]+array[0,1,1]+array[0,1,1]+array[1,0,2])
# HEY  ZEEL

# print(array.shape)
# (3, 3, 3)

# array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
#                 [['J','K','L'],['M','N','O'],['P','Q','R']],
#                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
# a=array[2][2][1]+array[0][1][1]+array[0][1][1]+array[1][0][2]
# print(a)
# ZEEL

a=np.array([[1,2,3,4],
            [5,6,7,8],
            [9,10,11,12],
            [13,14,15,16]])
# array[start:end:step]

# print(a[0:3:2])
# [[ 1  2  3  4]
#  [ 9 10 11 12]]

# print(a[::-1])
# [[13 14 15 16]
#  [ 9 10 11 12]
#  [ 5  6  7  8]
#  [ 1  2  3  4]]

# array[start:end:step(for rows),start:end:step(for cols)]
# print(a[:,0::1])
# [[ 1  2  3  4]
#  [ 5  6  7  8]
#  [ 9 10 11 12]
#  [13 14 15 16]]

# print(a[:,0:3:2])
# [[ 1  3]
#  [ 5  7]
#  [ 9 11]
#  [13 15]]

# print(a[:,-2])
# [ 3  7 11 15]

# print(a[1:3:,1:3:])
# [[ 6  7]
#  [10 11]]

# print(a[::,::-1])
# [[ 4  3  2  1]
#  [ 8  7  6  5]
#  [12 11 10  9]
#  [16 15 14 13]]

# print(a[::-1,::-1])
# [[16 15 14 13]
#  [12 11 10  9]
#  [ 8  7  6  5]
#  [ 4  3  2  1]]

# print(a[0:2,2:])
# [[3 4]
#  [7 8]]

# print(a[2:,0:2])
# [[ 9 10]
#  [13 14]]

# print(a[2:,2:])
# [[11 12]
#  [15 16]]