

## 异常处理

Python 使用 *try* 和 *except* 来正常处理错误。

![Try and Except](./try_except.png)

```python
try:
    print(10 + '5')
except:
    print('Something went wrong')
```

在上面的示例中，第二个操作数是一个字符串。我们可以将其更改为 float 或 int 以将其添加到数字中以使其工作。

但是，在没有任何更改的情况下，因为发生异常，所以将执行第二个块 *except* 。



```python
try:
    name = input('Enter your name:')
    year_born = input('Year you were born:')
    age = 2019 - year_born
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
```

使用多个 except 代码块来进入对应的异常情况处理



```python
try:
    name = input('Enter your name:')
    year_born = input('Year you born:')
    age = 2019 - int(year_born)
    print(f'You are {name}. And your age is {age}.')
except TypeError:
    print('Type error occur')
except ValueError:
    print('Value error occur')
except ZeroDivisionError:
    print('zero division error occur')
else:
    print('I usually run with the try block')
finally:
    print('I alway run.')
```

如果没有发生指定的异常，就会进入到 else 代码块，但不管如何都会执行 finally 代码块中。



## 打包和解包参数

### 解包

- `*` for tuples
- `**` for dictionaries

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e
lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(lst)) 
# TypeError: sum_of_five_nums() missing 4 required positional arguments: 'b', 'c', 'd', and 'e'

```

因为函数是将数字作为参数，而不是列表作为参数。因此我们可以使用 `*` 来解包参数。

```python
def sum_of_five_nums(a, b, c, d, e):
    return a + b + c + d + e

lst = [1, 2, 3, 4, 5]
print(sum_of_five_nums(*lst))  # 15
```

我们还可以在 range 内置函数中使用 解包

```python
numbers = range(2, 7)  # normal call with separate arguments
print(list(numbers)) # [2, 3, 4, 5, 6]

args = [2, 7]
numbers = range(*args)  # call with arguments unpacked from a list
print(numbers)      # [2, 3, 4, 5,6]
```



一个列表或者元组也可以这样子解包。

```python
countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin, sw, nor, *rest = countries
print(fin, sw, nor, rest)   # Finland Sweden Norway ['Denmark', 'Iceland']

numbers = [1, 2, 3, 4, 5, 6, 7]
one, *middle, last = numbers
print(one, middle, last)      #  1 [2, 3, 4, 5, 6] 7
```



字典解包

```python
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'

dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.
```



### 打包

有时我们永远不知道需要向 python 函数传递多少个参数。我们可以使用 packing 方法允许我们的函数接受无限数量或任意数量的参数。

```python
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s

print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28
```



```python
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))
```



## 在 Python 中展开

```python
lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, *lst_two]
print(lst)          # [0, 1, 2, 3, 4, 5, 6, 7]
```

## 枚举

使用 *enumerate* 内置函数来获取列表中每个项目的索引。

```python
for index, item in enumerate([20, 30, 40]):
    print(index, item)
```

## Zip

如果想在循环时组合列表。

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_veges = []
for f, v in zip(fruits, vegetables):
    fruits_and_veges.append({'fruit':f, 'veg':v})

print(fruits_and_veges)
```

```python
[{'fruit': 'banana', 'veg': 'Tomato'}, {'fruit': 'orange', 'veg': 'Potato'}, {'fruit': 'mango', 'veg': 'Cabbage'}, {'fruit': 'lemon', 'veg': 'Onion'}, {'fruit': 'lime', 'veg': 'Carrot'}]

```

