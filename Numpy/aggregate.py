import numpy as np

#! aggregate function = summarize data and typically
#                      return a single Value

a = np.array([[1,2,3,4,5],
              [6,7,8,9,10]])

# print(np.sum(a))
# 55

# print(np.mean(a))
# 5.5

# print(np.std(a))
# 2.8722813232690143
# Standard Deviation

# print(np.var(a))
# variance(Squer of standard Deviation)
# 8.25

# print(np.min(a))
# 1
# print(np.max(a))
# 10

# print(np.argmin(a))
# argument min(Position of Min Value)
# 0
# print(np.argmax(a))
# argument max(Position of Max Value)
# 9

# print(np.sum(a, axis=0))
# Sum of Col
# [ 7  9 11 13 15]
# print(np.sum(a, axis=1))
# sum of row
# [15 40]
