## 安装虚拟环境

要开始项目，最好有一个虚拟环境。虚拟环境可以帮助我们创建一个隔离或独立的环境。这将帮助我们避免跨项目依赖项的冲突。
如果你在终端上输入`pip freeze`，你会看到计算机上安装的所有软件包。如果我们使用 virtualenv，我们将只能访问特定于该项目的软件包。
打开你的终端并安装 `virtualenv`

```shell
pip install virtualenv
```

For Mac/Linux:

```shell
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project\$ virtualenv venv
```

For Windows:

```shell
C:\Users\User\Documents\30DaysOfPython\flask_project>python -m venv venv
```

## 激活虚拟环境

For Mac/Linux:

```shell
asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ source venv/bin/activate
```

For Windows Power Shell:

```shell
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\activate
```

For Windows Git bash:

```shell
C:\Users\User\Documents\30DaysOfPython\flask_project> venv\Scripts\. activate
```

激活以后就会显示

```shell
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$
```

当我们安装包的时候，在执行 `pip freeze`，就会发现只有虚拟环境里面的包

```shell
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython/flask_project$ pip freeze
Click==7.0
Flask==1.1.1
itsdangerous==1.1.0
Jinja2==2.10.3
MarkupSafe==1.1.1
Werkzeug==0.16.0
```

## 取消激活环境

```shell
(venv) asabeneh@Asabeneh:~/Desktop/30DaysOfPython$ deactivate
```
