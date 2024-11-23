## 正则表达式

正则表达式或 RegEx 是一种特殊的文本字符串，有助于在数据中查找模式。

```python
import re
```



## 在re模块里的方法

- *`re.match()`*: 仅在字符串第一行的开头搜索，如果找到则返回匹配的对象，否则返回 None。
- *`re.search`*: 如果字符串中的任意位置（包括多行字符串），则返回 match 对象。
- *`re.findall`*: 返回包含所有匹配项的列表
- *`re.split`*: 获取一个字符串，在匹配点拆分它，返回一个列表
- *`re.sub`*: **Replaces one or many matches within a string**

## match方法

```python
# syntac
re.match(substring, string, re.I)
# substring is a string or a pattern, string is the text we look for a pattern , re.I is case ignore
```

```python
import re

txt = 'I love to teach python and javaScript'

# 返回一个 Match 对象
match = re.match('I love to teach', txt, re.I) # 忽略大小写

print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>

# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach
```



## search方法

```python
# syntax
re.match(substring, string, re.I)
# substring is a pattern, string is the text we look for a pattern , re.I is case ignore flag
```

```python
import re

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It returns an object with span and match
match = re.search('first', txt, re.I)
print(match)  # <re.Match object; span=(100, 105), match='first'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (100, 105)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 100 105
substring = txt[start:end]
print(substring)       # first
```

它可以在整个文本中查找模式,Search 返回一个 match 对象，其中包含找到的第一个匹配项，否则返回 *None*。

## findall方法

查找所有匹配项

```python
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

# It return a list
matches = re.findall('language', txt, re.I)
print(matches)  # ['language', 'language']
```



## split方法

```python
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol
```

```python
['I am teacher and  I love teaching.', 'There is nothing as rewarding as educating and empowering people.', 'I found teaching more interesting than any other jobs.', 'Does this motivate you to be a teacher?']
```



## sub方法

替代子串

```python
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match_replaced = re.sub('Python|python', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

# OR
match_replaced = re.sub('[Pp]ython', 'JavaScript', txt, re.I)
print(match_replaced)  # JavaScript is the most beautiful language that a human being has ever created.

```

## 写一个正则表达式

要声明字符串变量，我们使用单引号或双引号。

声明 RegEx 变量 *r*。

```python
import re

regex_pattern = r'apple'
```

![Regular Expression cheat sheet](./regex.png)