## 函数定义

函数是一块可重复使用的代码块或者变成语句

## 声明和调用函数

```python
语法
# 声明一个函数
def function_name():
    codes
    codes


# 调用一个函数
function_name()
```

## 无参函数

```python
def print_hello_world():
    print("hello world")


print_hello_world()  # 调用一个函数
```

## 有返回值的函数

如果一个函数没有 `return` 语句，那么函数的返回值为 `None`。

```python
def generate_full_name ():
    first_name = 'hello_world'
    return first_name
print(generate_full_name())
```

## 有参数的函数

在一个函数中，我们可以传递不同的数据类型（数字、字符串、布尔值、列表、元组、字典或集合）作为参数。

```python
  # 语法
  # 声明一个函数
  def function_name(parameter):
    codes
    codes
  # 调用函数
  print(function_name(argument))
```

```python
  # 语法
  # 声明一个函数
  def function_name(para1, para2):
    codes
    codes
  # 调用函数
  print(function_name(arg1, arg2))
```

## 使用键值对传递参数

```python
def add_two_numbers (num1, num2):
    total = num1 + num2
    print(total)
print(add_two_numbers(num2 = 3, num1 = 2)) # 顺序无关紧要
```

## 带默认参数的函数

```python
def greetings (name = 'hello_world'):
    message = name + ', welcome to Python for Everyone!'
    return message
print(greetings()) # hello_world, welcome to Python for Everyone!
print(greetings('Asabeneh')) #Asabeneh, welcome to Python for Everyone!
```

## 不定数量的参数

可以通过在参数名前加上 * 来创建一个可以接受不定数量参数的函数。

```python
def sum_all_nums(*nums):
    total = 0
    for num in nums:
        total += num     # 相当于 total = total + num
    return total
print(sum_all_nums(2, 3, 5)) # 10
```

