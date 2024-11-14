## 创建字符串

任何用单引号、双引号或三引号括起来的数据都是字符串。

```python
greeting = 'Hello, World!'  # 字符串使用单引号或双引号构建，"Hello, World!"

multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
```



## 字符串串联

```python
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
```



## 字符串中的转译序列

- `\n`: 换行
- `\t`: 制表符(4个空格)
- `\\`: 反斜杠
- `\'`: 单引号
- `\"`: 双引号



## 字符串格式化

### format

```python
first_name = 'I'
last_name = 'Love'
language = 'Python'
formated_string = ' {} {} {}'.format(first_name, last_name, language)
```

### 字符串插值 / f-Strings

```python
a = 4
b = 3
print(f'{a} + {b} = {a +b}')
print(f'{a} / {b} = {a / b:.2f}')
```

## Python 字符串是字符序列

与其他 Python 有序对象一样 - 列表和元组 - 共享基本访问方法。

### 拆解字符

```python
language = 'Python'
a,b,c,d,e,f = language # 拆解字符串中的字符并赋值给变量
print(a) # P
print(b) # y
print(c) # t
print(d) # h
print(e) # o
print(f) # n
```

### 通过索引获取字符串中的字符

可以使用正索引和负索引，-1 是最后一个索引。

```python
language = 'Python'
first_letter = language[0]
print(first_letter) # P
```

### 字符串切片

```python
language = 'Python'
first_three = language[0:3] # 从零索引开始，直到 3 但不包括 3
print(first_three) #Pyt
```

### 字符串反转

```python
greeting = 'Hello, World!'
print(greeting[::-1]) # !dlroW ,olleH
```

### 切片时跳过字符

```python
language = 'Python'
pto = language[0:6:2] #
print(pto) # Pto
```



## 字符串方法

[字符串方法](https://docs.python.org/3.9/library/stdtypes.html#string-methods)



- capitalize(): 将字符串中的第一个字符转换为大写字母
- count(): 返回字符串中子字符串的出现次数，count(子字符串，start=..，end=..)。start 是计数的起始索引，end 是计数的最后一个索引。
- endswith(): 判断字符串是否以特定的子字符串结尾，返回 True 或 False
- expandtabs(): 用空格替换制表符，默认制表符大小为 8。它接受制表符大小参数
- find(): 返回子字符串第一次出现的索引，如果未找到则返回 -1
- rfind(): 返回子字符串最后一次出现的索引，如果未找到则返回 -1
- format(): 将字符串格式化为更美观的输出 有关字符串格式化的更多信息，请查看此[链接](https://www.programiz.com/python-programming/methods/string/format)
- index(): 返回子字符串的最小索引，附加参数表示起始和结束索引（默认为 0，字符串长度为 - 1）。如果未找到子字符串，则会引发 valueError。
- rindex(): 返回子字符串的最大索引，附加参数表示起始和结束索引（默认为 0，字符串长度为 - 1）。
- isalnum(): 判断字符串字符是否都是字母数字字符
- isalpha(): 判断字符串字符是否都是字母字符 (a-z and A-Z)
- isdecimal(): 判断符串中的所有字符是否都是十进制 (0-9)
- isdigit(): 判断字符串中的所有字符是否都是数字（0-9 和一些其他表示数字的 Unicode 字符）
- isnumeric(): 判断字符串中的所有字符是否都是数字或与数字相关（就像 isdigit()，只是接受更多符号，如 ½）
- isidentifier(): 判断有效的标识符 - 检查字符串是否是有效的变量名
- islower(): 判断字符串中的所有字母是否都是小写
- join(): 返回连接后的字符串
- strip(): 删除从字符串开头到结尾的所有给定字符
- replace(): 用给定的字符串替换子字符串
- split(): 使用给定的字符串或空格作为分隔符来拆分字符串
- title(): 返回标题大小写的字符串
- swapcase(): 将所有大写字符转换为小写字符，将所有小写字符转换为大写字符
- startswith(): 判断字符串是否以指定字符串开头

