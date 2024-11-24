## 类和对象

在 Python 中，一切都是对象，具有其属性和方法。程序中使用的数字、字符串、列表、字典、元组、集合等都是相应内置类的对象。
我们创建类来创建一个对象。类就像一个对象构造器，或者是创建对象的“蓝图”。
我们实例化一个类来创建一个对象。类定义了对象的属性和行为，而对象则代表了类。

## 创建一个类

```
# syntax
class ClassName:
  code goes here
```

```python
class Person:
    pass


print(Person)
```

## 创建一个对象

```python
p = Person()
print(p)
```

## 类的构造器

就像 Java 或 JavaScript 中的构造函数一样，Python 也有一个内置的 __init__() 构造函数。__init__ 构造函数有一个 self
参数，它是对当前类实例的引用。

```python
class Person:
    def __init__(self, name):
        # self allows to attach parameter to the class
        self.name = name


p = Person('Asabeneh')
print(p.name)
print(p)
```

## 对象方法

```python
class Person:
    def __init__(self, firstname, lastname, age, country, city):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}'


p = Person('Asabeneh', 'Yetayeh', 250, 'Finland', 'Helsinki')
print(p.person_info())

# output
# Asabeneh Yetayeh is 250 years old. He lives in Helsinki, Finland
```

## 对象默认方法

有时，你可能希望为对象方法设置默认值。如果我们在构造函数中为参数提供默认值，那么在没有参数的情况下调用或实例化类时，我们可以避免错误。

```python
class Person:
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki'):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.country = country
        self.city = city

    def person_info(self):
        return f'{self.firstname} {self.lastname} is {self.age} years old. He lives in {self.city}, {self.country}.'


p1 = Person()
print(p1.person_info())
p2 = Person('John', 'Doe', 30, 'Nomanland', 'Noman city')
print(p2.person_info())
```

## 类的继承

继承允许我们定义一个类，该类从父类继承所有方法和属性。父类或超类或基类是提供所有方法和属性的类。子类是从另一个或父类继承的类。

```python
class Student(Person):
    pass


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo')
print(s1.person_info())
```

我们没有在子类中调用`init()`
构造函数。如果我们没有调用它，我们仍然可以访问来自父类的所有属性。但是，如果我们调用了构造函数，我们可以通过调用`super`
来访问父类属性。

## 重写父类方法
我们可以在子类中添加新方法，或者通过在子类中创建相同的方法名来重写父类的方法。当我们添加init()函数时，子类将不再继承父类的init()函数。

```python
class Student(Person):
    def __init__(self, firstname='Asabeneh', lastname='Yetayeh', age=250, country='Finland', city='Helsinki',
                 gender='male'):
        self.gender = gender
        super().__init__(firstname, lastname, age, country, city)

    def person_info(self):
        gender = 'He' if self.gender == 'male' else 'She'
        return f'{self.firstname} {self.lastname} is {self.age} years old. {gender} lives in {self.city}, {self.country}.'


s1 = Student('Eyob', 'Yetayeh', 30, 'Finland', 'Helsinki', 'male')
s2 = Student('Lidiya', 'Teklemariam', 28, 'Finland', 'Espoo', 'female')
print(s1.person_info())

# Eyob Yetayeh is 30 years old. He lives in Helsinki, Finland.

```
