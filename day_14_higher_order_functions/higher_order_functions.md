## 高阶函数定义

**定义**：高阶函数是指以下至少满足其中一个条件的函数：

- 函数的参数是函数。
- 函数的返回值是函数。

### 函数作为参数

```python
def sum_numbers(nums):  # 普通函数
    return sum(nums)    # 使用内置函数sum的函数
 
def higher_order_function(f, lst):  # 将函数作为参数
    summation = f(lst) # 调用f函数，参数是lst
    return summation

result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15
```

### 函数作为返回值

利用函数名称来判断函数

```python
def square(x):          # 求平方函数
    return x ** 2

def cube(x):            # 求立方函数
    return x ** 3

def absolute(x):        # 求绝对值函数
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # 返回一个函数的高阶函数
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3
```

## Python 闭包

闭包是指一个函数（内部函数）能够记住并访问其外部函数的变量，即使外部函数已经返回。

Python 允许嵌套函数访问外部封闭函数的作用域，也就是说闭包允许函数访问 **外部函数的局部变量**，并在外部函数执行完毕后，依然能够记住这些变量。

那闭包是如何创建的?**闭包是通过在另一个封装函数内部嵌套函数，然后返回内部函数来创建的。**

```python
def add_ten():
    ten = 10  # 外部函数的局部变量
    def add(num):  #add_ten函数内部嵌套了一个函数（add)
        return num + ten # 这里ten来自add_ten函数，而且 add 函数能够访问 ten 这个变量的
    return add  # 返回内部函数
```

```python
closure_result = add_ten() # closure_result 这是一个闭包函数
print(closure_result(5))  # 15
print(closure_result(10))  # 20
```



## Python 装饰器

装饰器是一种设计模式，允许用户在 **不修改对象结构的情况下** 为其添加新功能。装饰器通常在你想要装饰的函数定义之前调用。

装饰器本质上是一个接受函数作为参数并返回一个新的函数的函数。

### 创建装饰器

要创建装饰器函数，我们需要一个**带有内部包装器函数**的外部函数。

```python
# 普通函数
def greeting():
    return 'Welcome to Python'
```

```python
# 带有内部包装器函数的外部函数
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper
```

```python
g = uppercase_decorator(greeting)
print(g())          # WELCOME TO PYTHON
```

使用装饰器实现

```python
'''这个装饰器函数是一个高阶函数，接收一个函数作为参数'''
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
```

将多个装饰器用于单个函数

```python
'''这些装饰器函数是高阶函数，接收函数作为参数'''

# 第一个装饰器
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

# 第二个装饰器
def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string_decorator
@uppercase_decorator     # 在此情况下，装饰器的顺序很重要 - .upper()函数不适用于列表
def greeting():
    return 'Welcome to Python'
print(greeting())   # WELCOME TO PYTHON
```



## 内置高阶函数

### map函数

`map` 函数用于将指定函数作用到给定序列（或可迭代对象）中的每个元素上，返回一个新的迭代器,接收一个函数和可迭代对象作为参数。

```python
    # 语法
    map(function, iterable)
```



```python
numbers = [1, 2, 3, 4, 5] # 可迭代对象
def square(x):
    return x ** 2
numbers_squared = map(square, numbers)
print(list(numbers_squared))    # [1, 4, 9, 16, 25]
```

```python
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # 可迭代对象

def change_to_upper(name):
    return name.upper()

names_upper_cased = map(change_to_upper, names)
print(list(names_upper_cased))    # ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
```

### Filter函数

`filter` 函数用于筛选序列中的元素，返回一个新的迭代器，包含所有使函数返回值为 `True` 的元素。

```python
# 语法
filter(function, iterable)
```

### Reduce函数

`reduce` 函数用于对序列中的元素进行累积操作（常用于聚合操作），它将一个二元函数应用于序列中的元素，从左到右地进行累积计算，最终返回一个结果。

```python
numbers_str = ['1', '2', '3', '4', '5']  # 可迭代对象
def add_two_nums(x, y):
    return int(x) + int(y)

total = reduce(add_two_nums, numbers_str)
print(total)    # 15
```

