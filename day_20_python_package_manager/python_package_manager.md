## 什么是pip

pip 全称 preferred installer program，是 python 的包管理器。

## 安装 pip

```shell
$ pip install pip
```

查看 pip 版本
```shell
$ pip --version
```

## 安装包和卸载包

```shell
# 安装
pip install <package_name>

# 卸载
pip uninstall <package_name>
```

## 查看包列表

```shell
pip list
```

## 展示包信息

```shell
pip show packagename
```

## pip 固化

生成已安装的 Python 软件包及其版本，输出适用于在需求文件中使用。requirements.txt 文件是一个应包含 Python 项目中所有已安装 Python 软件包的文件。

```shell
$ pip freeze
docutils==0.11
Jinja2==2.7.2
MarkupSafe==0.19
Pygments==1.6
Sphinx==1.2.2
```

## 读取一个url

安装 requests 模块

```shell
$ pip install requests
```

```python
import requests
url = 'https://restcountries.eu/rest/v2/all'  # countries api
response = requests.get(url)  # opening a network and fetching a data
print(response) # response object
print(response.status_code)  # status code, success:200
countries = response.json()
print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

```

## 创建一个包
包实际上是一个包含一个或多个模块文件的文件夹。
```
─ mypackage
    ├── __init__.py
    ├── arithmetic.py
    └── greet.py
```
