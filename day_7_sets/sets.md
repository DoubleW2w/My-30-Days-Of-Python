## 创建集合

```python
# 语法
st = set()

# 语法
st = {'item1', 'item2', 'item3', 'item4'}

```

## 获取集合长度

len()

## 检查项目

```python
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
print("Does set st contain item3? ", 'item3' in st)  # Does set st contain item3? True
```

## 向集合中添加项目

添加单个元素

```python
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
st.add('item5')
```

添加多个元素

```python
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
st.update(['item5', 'item6', 'item7'])
```

## 从集合中移除项目

```python
# 语法
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
```

```python
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # 从集合中移除一个随机元素
```

## 清空集合中的项目

`clear()`

## 删除集合

`del st`

## 将列表转换为集合

```python
fruits = ['banana', 'orange', 'mango', 'lemon', 'orange', 'banana']
fruits = set(fruits)  # {'mango', 'lemon', 'banana', 'orange'}
```

## 合并集合

使用 `union()` 或 `update()` 方法来合并两个集合。

## 查找交集项目

```python
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2)  # {'item3', 'item2'}
```

## 检查子集和超集

一个集合可以是另一个集合的子集或超集：

子集: `issubset()`
超集: `issuperset()`

## 检查两个集合之间的差异

```python
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1)  # set()
st1.difference(st2)  # {'item1', 'item4'} => st1\st2
```

## 查找两个集合之间的对称差异

它返回一个包含两个集合中所有项的集合，除了同时出现在两个集合中的项

```python
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# 意思是 (A\B)∪(B\A)
st2.symmetric_difference(st1)  # {'item1', 'item4'}
```

## 合并集合
```python
# 语法
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.isdisjoint(st1) # 错误
```
