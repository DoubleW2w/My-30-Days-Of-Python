字典是一种由无序、可修改（可变）的键值对组成的数据类型。


## 从字典中删除键值对
`pop(key)`: 删除具有指定键名的项目
`popitem()`: 删除最后一个项目
`del`: 删除具有指定键名的项目

## 将字典改变为项目列表

```python
# 语法
dct = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 'value4'}
print(dct.items())  # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
```

## 清空字典

```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
```

## 复制字典

```python
# 语法
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
```
