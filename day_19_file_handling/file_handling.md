使用 open() 函数来处理文件

## 打开一个文件

```python
# Syntax
open('filename', mode)  # mode(r, a, w, x, t,b)  could be to read, write, update
```

- "r" - 读取一个文件，如果文件不存在会报错
- "a" - 追加文件内容，如果文件不存在会创建
- "w" - 写入文件内容，如果文件不存在会创建
- "x" - 创建一个文件，如果文件存在会报错
- "t" - 文本模式
- "b" - 二进制模式

## 读取一个文件

```python
f = open('./files/reading_file_example.txt')
txt = f.read()
print(type(txt))
print(txt)
f.close()
```

```
# output
<class 'str'>
This is an example to show how to open a file and read.
This is the second line of the text.
```

`readline()`: 读取首行

`readlines()`：逐行读取整个文本，并返回一个行列表

```python
f = open('./files/reading_file_example.txt')
lines = f.readlines()
print(type(lines))
print(lines)
f.close()
```

```python
f = open('./files/reading_file_example.txt')
lines = f.read().splitlines()
print(type(lines))
print(lines)
f.close()
```

## with 的方式打开文件

使用 with 打开文件的新方法 - 自行关闭文件

```python
with open('./files/reading_file_example.txt') as f:
    lines = f.read().splitlines()
    print(type(lines))
    print(lines)
```

## 删除文件

想删除一个文件，我们使用 os 模块。

```python
import os

os.remove('./files/example.txt')
```

如果文件不存在，则 remove 方法将引发错误，因此最好使用如下条件：

```python
import os

if os.path.exists('./files/example.txt'):
    os.remove('./files/example.txt')
else:
    print('The file does not exist')
```

## json格式的文件

```python
# 字典
person_dct = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# JSON: 字符串组成的字典
person_json = "{'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'skills': ['JavaScrip', 'React', 'Python']}"

# we use three quotes and make it multiple line to make it more readable
person_json = '''{
    "name":"Asabeneh",
    "country":"Finland",
    "city":"Helsinki",
    "skills":["JavaScrip", "React","Python"]
}'''
```

## 把JSON变成字典

```python
import json

# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''

# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])
```

## 把字典变成JSON

```python
import json

# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
# let's convert it to  json
person_json = json.dumps(person, indent=4)  # indent could be 2, 4, 8. It beautifies the json
print(type(person_json))
print(person_json)
```

## 保存为json文件

```python
import json

# python dictionary
person = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}
with open('./files/json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person, f, ensure_ascii=False, indent=4)
```

## csv文件

CSV 代表逗号分隔值。CSV 是一种用于存储表格数据（例如电子表格或数据库）的简单文件格式。CSV 是数据科学中一种非常常见的数据格式。

```python
import csv

with open('./files/csv_example.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')  # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')
```

## xlsx 文件

要读取 excel 文件，我们需要安装 xlrd 包。我们将在介绍使用 pip 安装包之后介绍这一点。

```python
import xlrd

excel_book = xlrd.open_workbook('sample.xls)
print(excel_book.nsheets)
print(excel_book.sheet_names)
```

## xml文件

```
<?xml version="1.0"?>
<person gender="female">
  <name>Asabeneh</name>
  <country>Finland</country>
  <city>Helsinki</city>
  <skills>
    <skill>JavaScrip</skill>
    <skill>React</skill>
    <skill>Python</skill>
  </skills>
</person>
```

```python
import xml.etree.ElementTree as ET
tree = ET.parse('./files/xml_example.xml')
root = tree.getroot()
print('Root tag:', root.tag)
print('Attribute:', root.attrib)
for child in root:
    print('field: ', child.tag)
```
