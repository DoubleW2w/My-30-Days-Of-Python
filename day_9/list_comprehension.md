## 列表推导式

列表推导式是一种从序列中创建列表的简洁方式。

## 字符串转换为列表

```python
# 一种方法
language = 'Python'
lst = list(language)  # 将字符串转换为列表
print(type(lst))      # list
print(lst)            # ['P', 'y', 't', 'h', 'o', 'n']
```

```python
# 第二种方法: 列表推导式
lst = [i for i in language]
print(type(lst))     # list
print(lst)           # ['P', 'y', 't', 'h', 'o', 'n']
```

## 生成数字列表

```python
# 生成数字
numbers = [i for i in range(11)]  # 生成从0到10的数字
print(numbers)                    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 也可以在迭代过程中进行数学运算
squares = [i * i for i in range(11)]
print(squares)                    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 还可以生成元组列表
numbers = [(i, i * i) for i in range(11)]
print(numbers)                    # [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]
```

## if 表达式结合

```python
# 过滤数字：让我们从下面的列表中过滤出正偶数
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_numbers = [i for i in range(21) if i % 2 == 0 and i > 0]
print(positive_even_numbers)           # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```

## Lambda 函数

Lambda 函数是没有名字的小匿名函数。它可以接受任意数量的参数，但只能有一个表达式。

```python
# 语法
x = lambda param1, param2, param3: param1 + param2 + param3
print(x(arg1, arg2, arg3))
```

### 例子

```python
# 命名函数
def add_two_nums(a, b):
    return a + b

print(add_two_nums(2, 3))  # 5

# 让我们将上述函数更改为 lambda 函数
add_two_nums = lambda a, b: a + b
print(add_two_nums(2, 3))  # 5
```

### Lambda 函数在另一个函数中

```python
def power(x):
    return lambda n: x ** n

cube = power(2)(3)   # 函数 power 现在需要两个单独的括号中的参数
print(cube)          # 8
two_power_of_five = power(2)(5)
print(two_power_of_five)  # 32
```

