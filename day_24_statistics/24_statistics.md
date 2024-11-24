`## 介绍

[官方文档 statistics 模块](https://docs.python.org/3/library/statistics.html#module-statistics)

Python statistics 模块提供了用于计算数值数据数学统计的函数。
该模块并不打算与第三方库（如 NumPy、SciPy）或针对专业统计人员的全面商业统计软件包（如
Minitab、SAS 和 Matlab）竞争。它的定位是图形和科学计算器的级别。

## 数据

什么是数据？数据是为某种目的（通常是分析）而收集和转换的任何一组字符。
它可以是任何字符，包括文本和数字、图片、声音或视频。如果数据没有放在上下文中，它对人类或计算机都没有任何意义。

## Numpy

安装Numpy

```shell
pip install numpy
```

### 创建 int numpy 数组

```python
import numpy as np

# Creating python List
python_list = [1, 2, 3, 4, 5]

# Checking data types
print('Type:', type(python_list))  # <class 'list'>
#
print(python_list)  # [1, 2, 3, 4, 5]

numpy_array_from_list = np.array(python_list)
print(type(numpy_array_from_list))  # <class 'numpy.ndarray'>
print(numpy_array_from_list)  # array([1, 2, 3, 4, 5])
```

### 创建 float numpy 数组

```python
    # Python list
python_list = [1, 2, 3, 4, 5]

numy_array_from_list2 = np.array(python_list, dtype=float)
print(numy_array_from_list2)  # array([1., 2., 3., 4., 5.])
```

### 创建 boolean numpy 数组

```python
    numpy_bool_array = np.array([0, 1, -1, 0, 0], dtype=bool)
print(numpy_bool_array)  # array([False,  True,  True, False, False])
```

### 使用numpy 创建多维数组

```python
    two_dimensional_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
numpy_two_dimensional_list = np.array(two_dimensional_list)
print(type(numpy_two_dimensional_list))
print(numpy_two_dimensional_list)

"""
    <class 'numpy.ndarray'>
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
"""
```

### 将numpy数组转换为list

```python
# We can always convert an array back to a python list using tolist().
np_to_list = numpy_array_from_list.tolist()
print(type(np_to_list))  # <class 'list'>
print('one dimensional array:', np_to_list)  # one dimensional array: [1, 2, 3, 4, 5]
print('two dimensional array: ',
      numpy_two_dimensional_list.tolist())  # two dimensional array:  [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
```

### 使用元组创建 numpy数组

```python
# Numpy array from tuple
# Creating tuple in Python
python_tuple = (1, 2, 3, 4, 5)
print(type(python_tuple))  # <class 'tuple'>
print('python_tuple: ', python_tuple)  # python_tuple:  (1, 2, 3, 4, 5)

numpy_array_from_tuple = np.array(python_tuple)
print(type(numpy_array_from_tuple))  # <class 'numpy.ndarray'>
print('numpy_array_from_tuple: ', numpy_array_from_tuple)  # numpy_array_from_tuple:  [1 2 3 4 5]
```

### shape 方法

shape 方法以元组形式提供数组的形状。第一个元素是行，第二个元素是列。
如果数组只是一维的，它将返回数组的大小。

```python
nums = np.array([1, 2, 3, 4, 5])
print(nums)
print('shape of nums: ', nums.shape)
print(numpy_two_dimensional_list)
print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
three_by_four_array = np.array([[0, 1, 2, 3],
                                [4, 5, 6, 7],
                                [8, 9, 10, 11]])
print(three_by_four_array.shape)
```

```
    [1 2 3 4 5]
    shape of nums:  (5,)
    [[0 1 2]
     [3 4 5]
     [6 7 8]]
    shape of numpy_two_dimensional_list:  (3, 3)
    (3, 4)
```

### numpy数组的数据类型

数据类型：str, int, float, complex, bool, list, None

```python
int_lists = [-3, -2, -1, 0, 1, 2, 3]
int_array = np.array(int_lists)
float_array = np.array(int_lists, dtype=float)

print(int_array)
print(int_array.dtype)
print(float_array)
print(float_array.dtype)
```

```
    [-3 -2 -1  0  1  2  3]
    int64
    [-3. -2. -1.  0.  1.  2.  3.]
    float64
```

### numpy 数组的大小

```python
numpy_array_from_list = np.array([1, 2, 3, 4, 5])
two_dimensional_list = np.array([[0, 1, 2],
                                 [3, 4, 5],
                                 [6, 7, 8]])

print('The size:', numpy_array_from_list.size)  # 5
print('The size:', two_dimensional_list.size)  # 9

```

## 数学操作

NumPy 数组并不完全像 Python 列表。在 Python 列表中执行数学运算，我们必须遍历各项，但 numpy 允许无需循环即可进行任何数学运算。

## 检查数据类型

```python
# Int,  Float numbers
numpy_int_arr = np.array([1, 2, 3, 4])
numpy_float_arr = np.array([1.1, 2.0, 3.2])
numpy_bool_arr = np.array([-3, -2, 0, 1, 2, 3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)
```

```
 int64
    float64
    bool
```

## 数据类型转换

```python
numpy_int_arr = np.array([1,2,3,4], dtype = 'float')
numpy_int_arr  # array([1., 2., 3., 4.])

```
```python
numpy_int_arr = np.array([1., 2., 3., 4.], dtype = 'int')
numpy_int_arr  #     array([1, 2, 3, 4])
```

```python
np.array([-3, -2, 0, 1,2,3], dtype='bool')
# array([ True,  True, False,  True,  True,  True])
```

```python
numpy_float_list.astype('int').astype('str')
#  array(['1', '2', '3'], dtype='<U21')
```
