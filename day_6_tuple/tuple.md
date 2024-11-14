## 如何创建元组

```python
# 语法
empty_tuple = ()
# 或使用元组构造函数
empty_tuple = tuple()
```

## 元组长度

```python
# 语法
tpl = ('item1', 'item2', 'item3')
len(tpl)
```

## 获取元组项、元组切片

## 将元组更改为列表
```python
# 语法
tpl = ('item1', 'item2', 'item3','item4')
lst = list(tpl)
```
## 检索元组中的项

```python
# 语法
tpl = ('item1', 'item2', 'item3','item4')
'item2' in tpl # True
```

## 连接元组
```python
# 语法
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
```

## 删除元组
```python
# 不能删除元组中的单个项，但可以使用 del 删除元组本身。
# 语法
tpl1 = ('item1', 'item2', 'item3')
del tpl1
```
