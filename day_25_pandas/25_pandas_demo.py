import pandas as pd, numpy as np

# 创建pd，使用默认的index
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
s = pd.Series(nums)
print(s)

# 自定义index
s = pd.Series(nums, index=[1, 2, 3, 4, 5, 6, 7, 8, 9])
print(s)

fruits = ['Orange', 'Banana', 'Mango']
fruits = pd.Series(fruits, index=[1, 2, 3])
print(fruits)

# 从字典创建pd series
dct = {'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki'}
s = pd.Series(dct)
print(s)

# 创建一个常值的 pd Series
s = pd.Series(10, index=[1, 2, 3])
print(s)

# 创建一个pd Series 使用 linspace
s = pd.Series(np.linspace(5, 20, 10))  # linspace(starting, end, items)
print(s)

# DataFrames

# 从列表创建DataFrames

data = [
    ['Asabeneh', 'Finland', 'Helsink'],
    ['David', 'UK', 'London'],
    ['John', 'Sweden', 'Stockholm']
]
df = pd.DataFrame(data, columns=['Names', 'Country', 'City'])
print(df)

# 从列表创建DataFrame

data = {'Name': ['Asabeneh', 'David', 'John'], 'Country': [
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data)
print(df)

# 从列表字典创建DataFrame

data = [
    {'Name': 'Asabeneh', 'Country': 'Finland', 'City': 'Helsinki'},
    {'Name': 'David', 'Country': 'UK', 'City': 'London'},
    {'Name': 'John', 'Country': 'Sweden', 'City': 'Stockholm'}]
df = pd.DataFrame(data)
print(df)

# 读取CSV文件

df = pd.read_csv('../data/weight-height.csv')
# print(df)

# 读取首5行

print(df.head())

# 后5行
print(df.tail())

# 10000行 3列
print(df.shape)

# 所有的列
print(df.columns)

# describe() 方法提供了数据集的描述性统计值。
heights = df['Height']
print(heights.describe())

"""
修改 DataFrame
- 创建
- 添加一个新列到DataFrame中
- 删除一个列
- 修改现有列
"""

data = [
    {"Name": "Asabeneh", "Country": "Finland", "City": "Helsinki"},
    {"Name": "David", "Country": "UK", "City": "London"},
    {"Name": "John", "Country": "Sweden", "City": "Stockholm"}]
df = pd.DataFrame(data)
print(df)

# 添加一列
weights = [74, 78, 69]
df['Weight'] = weights
print(df)

# 再添加一列
heights = [173, 175, 169]
df['Height'] = heights
print(df)

# 修改一列
df['Height'] = df['Height'] * 0.01
print(df)
