## while 循环

```python
# prints from 0 to 4
count = 0
while count < 5:
    count = count + 1
```

## while 和 else

想要在循环条件变为false时运行特定的代码块，我们可以使用else关键字。

```python
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
```

## break 关键字

break 关键字退出循环

```python
count = 0
while count < 5:
    count = count + 1
    if count == 3:
        break
```

## for 循环

```python
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers:  # number是引用列表项的临时名称，仅在此循环中有效
    print(number)  # number将会被逐行打印，从0到5
```

```python
language = 'Python'
for letter in language:
    print(letter)

for i in range(len(language)):
    print(language[i])
```

```python
numbers = (0, 1, 2, 3, 4, 5)
for number in numbers:
    print(number)
```

```python
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    print(key)  # 仅输出键

for key, value in person.items():
    print(key, value)  # 这样我们可以在迭代的过程中同时访问键和值
```

## range 函数

`range()` 函数用于生成一个序列的数字。
`_range(start, end, step)_`函数接受三个参数：起始值、结束值和步长。

## for和else

```python
# syntax
for iterator in range(start, end, step):
    do
    something
else:
    print('The loop ended')
```
