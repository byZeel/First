import pandas as pd
# print(pd.__version__)
# print(pd.__version__)
# data= [100,200,300]
# 0    100
# 1    200
# 2    300
# dtype: int64
# data= [100.1,200.3,300.5]
# 0    100.1
# 1    200.3
# 2    300.5
# dtype: float64
# data= [True,False,True]
# 0     True
# 1    False
# 2     True
# dtype: bool
# data= ["A","B","C"]
# 0    A
# 1    B
# 2    C
# dtype: str

#? Series = Pandas 1-Dimensional labeled array that can hold any data type
#?          think of it like a single column in spreadsheet (1-Dimensional)

# data= [100,200,300]

# s=pd.Series(data,index=[1,2,3])
# 1    100
# 2    200
# 3    300
# dtype: int64
# s=pd.Series(data,index=["a","b","c"])
# a    100
# b    200
# c    300
# dtype: int64

# print(s.loc["a"])
# location by s
# 100

# s.loc["c"]=400
# print(s)
# a    100
# b    200
# c    400
# dtype: int64

# print(s.iloc[0])
# intiger location
# # 100
# print(s.iloc[1])
# #200
# print(s.iloc[2])
# #300

# data= [100,200,300,400,500]
# s=pd.Series(data,index=["a","b","c","d","e"])
# print(s[s>=200])
# b    200
# c    300
# d    400
# e    500

# data= [100,200,300,400,500]
# s=pd.Series(data,index=["a","b","c","d","e"])
# print(s[(s>=200) & (s<=300)])
# b    200
# c    300
# dtype: int64

# data= {"Day 1":100,"Day 2":200,"Day 3":300,"Day 4":400,"Day 5":500}
# s=pd.Series(data,index=["a","b","c","d","e"])
# print(s)
# a   NaN
# b   NaN
# c   NaN
# d   NaN
# e   NaN
# dtype: float64

data= {"Day 1":100,"Day 2":200,"Day 3":300,"Day 4":400,"Day 5":500}
s=pd.Series(data)
s.loc["Day 4"] += 500
print(s)
# Day 1    100
# Day 2    200
# Day 3    300
# Day 4    900
# Day 5    500
# dtype: int64

