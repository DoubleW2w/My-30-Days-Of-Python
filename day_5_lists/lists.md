## 列表

Python 中有四种集合数据类型：

List：有序且可变的集合。允许重复的成员。
Tuple：有序且不可变的集合。允许重复的成员。
Set：无序、不可索引且不可变的集合，但我们可以向集合中添加新项。不允许重复的成员。
Dictionary：无序、可变且可索引的集合。不允许重复的成员。


### 如何创建列表

```python
# 语法
lst = list()

# 语法
lst = []
```



### 拆解列表项

```python
lst = ['item1','item2','item3', 'item4', 'item5']
first_item, second_item, third_item, *rest = lst
print(first_item)     # item1
print(second_item)    # item2
print(third_item)     # item3
print(rest)           # ['item4', 'item5']
```

### 列表切分

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
all_fruits = fruits[0:4] # 返回所有项
#与上面返回值相同
all_fruits = fruits[0:] # 如果不指定结束索引，将返回从开始到最后一项的所有项
orange_and_mango = fruits[1:3] # 不包含第一项
orange_mango_lemon = fruits[1:]
orange_and_lemon = fruits[::2] # 我们使用了第三个参数，步长。 每两项取一条 - ['banana', 'mango']
```

### 修改、检索、添加、插入、移除列表项

```python
# 修改
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits[0] = 'avocado'
print(fruits)       #  ['avocado', 'orange', 'mango', 'lemon']
```

```python
# 检索
fruits = ['banana', 'orange', 'mango', 'lemon']
does_exist = 'banana' in fruits
print(does_exist)  # True
```

```python
# 添加
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.append('apple')
print(fruits)           # ['banana', 'orange', 'mango', 'lemon', 'apple']
```
```python
# 插入
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # 在 orange 。 mango 中插入 apple
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
```

```python
# 移除
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana']
fruits.remove('banana')
print(fruits)  # ['orange', 'mango', 'lemon', 'banana'] - 此方法删除列表中第一次出现的项
```

### pop

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.pop()
print(fruits)       # ['banana', 'orange', 'mango']

fruits.pop(0)
print(fruits)       # ['orange', 'mango']
```

### Del 删除列表项

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[0]
print(fruits)       # ['orange', 'mango', 'lemon', 'kiwi', 'lime']
del fruits[1]
print(fruits)       # ['orange', 'lemon', 'kiwi', 'lime']
del fruits[1:3]     # 这将删除给定索引之间的项，因此不会删除索引为 3 的项!
print(fruits)       # ['orange', 'lime']
del fruits
print(fruits)       # 这里会提示: NameError: name 'fruits' is not defined
```

### 清空

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.clear()
print(fruits)       # []
```


### 列表复制

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits_copy = fruits.copy()
print(fruits_copy)       # ['banana', 'orange', 'mango', 'lemon']
```

### 连接列表

```python
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5,-4,-3,-2,-1]
integers = negative_numbers + zero + positive_numbers
print(integers) # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
```

```python
num1 = [0, 1, 2, 3]
num2= [4, 5, 6]
num1.extend(num2)
print('Numbers:', num1) # Numbers: [0, 1, 2, 3, 4, 5, 6]
```

### 统计列表项

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.count('orange'))   # 1
```

### 查找项的索引

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
print(fruits.index('orange'))   # 1
```

### 列表反转

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.reverse()
print(fruits) # ['lemon', 'mango', 'orange', 'banana']
```

### 列表排序

```python
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # 按字母排序， ['banana', 'lemon', 'mango', 'orange']
```
