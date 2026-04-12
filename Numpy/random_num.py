import numpy as np

# rng = np.random.default_rng(seed=1)
#? when you want to reproduce same result

# rng = np.random.default_rng()

# print(rng.integers(1,101))
# 23
# print(rng.integers(low=1, high=101, size=3))
# [12 26 12]
# print(rng.integers(low=1, high=101, size=(3,2)))
# [[81 90]
#  [64  3]
#  [23 92]]

# np.random.seed(1)
# np.random.seed(seed=1)
# print(np.random.uniform(low = -1, high=1, size=(3,2)))
#? uniform destribution

rng = np.random.default_rng()

# array = np.array([1,2,3,4,5])
# rng.shuffle(array)
# print(array)

# fruits = np.array(["apple", "orange", "banana", "mango", "pineapple"])
# fruits = rng.choice(fruits, size= 3)
# fruits = rng.choice(fruits, size= (3,3))
# print(fruits)

fruits = np.array(["🍎","🍊","🍌","🍍","🥭"])
fruits = rng.choice(fruits, size= (3,3))
print(fruits)