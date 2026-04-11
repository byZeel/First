import numpy as np

# ! filtering = Refers to the process of selecting elements
# !            from an array that match a given condition

ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                 [39, 22, 15, 99, 18, 19, 20, 21]])

# teenagers = ages[ages < 18]
# [17 16 15]
# adults = ages[(ages >= 18) & (ages <= 65)]
# [21 19 20 30 18 65 39 22 18 19 20 21]
# adults = ages[(ages < 18) | (ages > 65)]
# [17 16 15 99]
# senior = ages[ages >= 65]
# [65 99]
# evens = ages[ ages % 2 == 0]
# [20 16 30 18 22 18 20]
# odds = ages[ ages % 2 != 0]
# [21 17 19 65 39 15 99 19 21]

adults = np.where(ages >= 18, ages, np.nan)
#? (condition, input/array, fillvalue/replacevalue also use -1,np.nan)

print(adults)


