## Boolean

布尔类型表示两个值之一：*True* 或 *False*。

## 运算符

[w3school](https://www.w3schools.com/python/python_operators.asp)

- 赋值运算符

- 算数运算符

```python
加(+)： a + b
减(-)： a - b
乘(*)： a * b
除(/)： a / b
模运算(%)： a % b
整除(//)： a // b
指数运算(**)： a ** b
```

- 比较运算符

- 逻辑运算符

Python 使用关键字 *and*、*or* 和 *not* 作为逻辑运算符


---
python数据类型

**`int`**（整数）：用于表示整数值。例子：`5`, `-42`, `1000`

**`float`**（浮动数）：用于表示带小数的数字。例子：`3.14`, `-0.5`, `2.0`

**`complex`**（复数）：用于表示复数，包含实部和虚部。例子：`3+4j`, `2-7j`

**`str`**（字符串）：用于表示文本数据，是不可变的序列。例子：`"hello"`, `"Python"`

**`list`**（列表）：用于表示有序的元素集合，可以包含不同类型的元素，且是可变的。例子：`[1, 2, 3]`, `['apple', 'banana', 'cherry']`

**`tuple`**（元组）：类似于列表，但元组是不可变的。例子：`(1, 2, 3)`, `('a', 'b', 'c')`

**`set`**（集合）：无序且不重复的元素集合，元素可以是不可变数据类型。例子：`{1, 2, 3}`, `{'apple', 'banana'}`

**`frozenset`**（冻结集合）：与 `set` 类似，但它是不可变的。例子：`frozenset([1, 2, 3])`

**`dict`**（字典）：用于表示键值对的集合，是无序的。例子：`{'name': 'Alice', 'age': 25}`

**`bool`**（布尔）：表示逻辑值，只有两个值：`True` 和 `False`。

**`bytes`**：不可变的字节序列，通常用于处理原始数据。例子：`b'hello'`

**`bytearray`**：可变的字节序列。例子：`bytearray([65, 66, 67])`

**`memoryview`**：提供对字节对象的内存视图。例子：`memoryview(b'hello')`

**`None`**：表示空值或无值。例子：`None`



print函数打印

```python
print("Hello, World!")  # 输出: Hello, World!
```

```python
name = "Alice"
age = 25
print("Name:", name, "Age:", age)
```

```python
#  sep 参数，用来定义多个参数之间的分隔符,默认是空格
print("apple", "banana", "cherry", sep=", ")
```

```python
name = "Alice"
age = 25
print(f"Name: {name}, Age: {age}")
```

```python
name = "Alice"
age = 25
print("Name: {}, Age: {}".format(name, age))
```

