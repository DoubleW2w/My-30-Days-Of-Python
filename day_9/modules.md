## 模块定义

模块是包含一组代码或一组函数的文件，可以包含在一个应用程序中。



## 创建模块

在一个 Python 脚本中编写代码并保存为 `.py` 文件

```python
# mymodule.py 文件
def generate_full_name(firstname, lastname):
    return firstname + ' ' + lastname
```

在项目目录中创建 `main.py` 文件并导入 `mymodule.py` 文件。

## 导入模块

```python
# main.py 文件
import mymodule
print(mymodule.generate_full_name('Asabeneh', 'Yetayeh')) # Asabeneh Yetayeh
```

## 从模块中导入函数

```python
# main.py 文件
from mymodule import generate_full_name, sum_two_nums, person, gravity
print(generate_full_name('Asabneh','Yetayeh'))
print(sum_two_nums(1,9))
```

可以通过 as 关键字进行模块重命名

```python
# main.py 文件
from mymodule import generate_full_name as fullname, sum_two_nums as total, person as p, gravity as g
print(fullname('Asabneh','Yetayeh'))
print(total(1, 9))
```

## 导入内置模块

一些常见的内置模块：*math*、*datetime*、*os*、*sys*、*random*、*statistics*、*collections*、*json*、*re*

### OS模块

OS 模块提供了创建、更改当前工作目录和删除目录（文件夹）、获取其内容、更改和识别当前目录的函数。

```python
# 导入模块
import os
# 创建目录
os.mkdir('directory_name')
# 更改当前目录
os.chdir('path')
# 获取当前工作目录
os.getcwd()
# 删除目录
os.rmdir()
```

### sys模块

sys 模块提供用于操作 Python 运行时环境不同部分的函数和变量。

```python
# 退出 sys
sys.exit()
# 知道最大整数变量
sys.maxsize
# 知道环境路径
sys.path
# 知道使用的 Python 版本
sys.version
```

### 统计模块

统计模块提供用于数值数据的数学统计的函数。这个模块中定义的流行统计函数：*mean*、*median*、*mode*、*stdev* 等。

```python
from statistics import * # 导入所有统计模块
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3
```

### 数学模块

```python
import math
print(math.pi)           # 3.141592653589793, pi 常数
print(math.sqrt(2))      # 1.4142135623730951, 平方根
print(math.pow(2, 3))    # 8.0, 指数函数
print(math.floor(9.81))  # 9, 向下取整
print(math.ceil(9.81))   # 10, 向上取整
print(math.log10(100))   # 2, 以 10 为底的对数
```

### 字符串模块

```python
import string
print(string.ascii_letters) # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
print(string.digits)        # 0123456789
print(string.punctuation)   # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```

### 随机模块

```python
from random import random, randint
print(random())   # 它不需要任何参数；它返回一个介于 0 和 0.9999 之间的值
print(randint(5, 20)) # 它返回一个介于 [5, 20] 之间的随机整数（含边界）
```

