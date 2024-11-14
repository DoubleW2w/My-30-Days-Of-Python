"""
1.将字符串 'Thirty', 'Days', 'Of', 'Python' 连接为一个字符串 'Thirty Days Of Python'。
"""

print("thirty".join("Days").join("of").join("python"))


"""
2.将字符串 'Coding', 'For', 'All' 连接为一个字符串 'Coding For All'。
"""
print("Coding " + "For " + "All")


"""
声明一个名为 company 的变量，并将其赋值为初始值 "Coding For All"。
"""
company = "Coding For All"

"""
使用 print() 打印变量 company。
"""
print(company)

"""
使用 len() 方法和 print() 打印 company 字符串的长度。
"""
print(f"company的长度是{len(company)}")

"""
使用 upper() 方法将所有字符更改为大写字母。
"""
text = "abCd"
print(text.upper())
"""
使用 lower() 方法将所有字符更改为小写字母。
"""
print(text.lower())


# 使用 capitalize()、title() 和 swapcase() 方法格式化字符串 Coding For All。
text = "Coding For All"
print(text.capitalize())
print(text.title())
print(text.swapcase())


# 切片出 Coding For All 字符串的第一个单词。
text = "Coding For All"
print(text[0:6])


# 使用 index、find 或其他方法检查 Coding For All 字符串是否包含单词 Coding。

text = "Coding For All"
print(text.index("Coding"))
print(text.find("Coding"))

# 将字符串 'Coding For All' 中的单词 coding 替换为 Python。
text = "Coding For All"
print(text.replace("Coding", "Python"))

# 使用 replace 方法或其他方法将 Python for Everyone 替换为 Python for All。

text = "Python for Everyone"
new_text = text.replace("Everyone", "All")
print(new_text)

text = "Python for Everyone"
new_text = text[:13] + "All"  # 切片前13个字符，再加上替换的部分
print(new_text)


# 使用空格作为分隔符拆分字符串 'Coding For All'。
text = "Coding For All"
print(text.split(sep=" "))


# 在逗号处拆分字符串 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'。
text = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(text.split(","))


# 字符串 Coding For All 中索引 0 处的字符是什么。
text = "Coding For All"
print(text[0])

# 字符串 Coding For All 的最后一个索引是什么。
text = "Coding For All"
print(text[-1])


# 为字符串 'Python For Everyone' 创建首字母缩略词或缩写

phrase = "Python For Everyone"

# 分割字符串为单词，并取每个单词的首字母
acronym = "".join([word[0].upper() for word in phrase.split()])

print(acronym)


# 使用索引确定 'Coding For All' 中 C 第一次出现的位置。
text = "Coding For All"
print(text.index("C"))
print(text.find("C"))

# 使用 rfind 确定 'Coding For All People' 中 l 最后一次出现的位置。
text = "Coding For All People"
print(text.rfind("l"))

# 删除以下句子中短语 'because because because'：'You cannot end a sentence with because because because is a conjunction'
text = "You cannot end a sentence with because because because is a conjunction"
print(text.replace("because because because", ""))

#'Coding For All' 是否以子字符串 Coding 开头？
print("Coding For All".startswith("Coding"))
# 'Coding For All' 是否以子字符串 coding 结尾？
print("Coding For All".endswith("Coding"))

# '   Coding For All      '  , 删除给定字符串中左右空格。
print("   Coding For All      ".strip())

"""
使用制表符专业序列输出以下内容。
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
"""
print(f"Name\tAge\tCountry\tCity")
print(f"Asabeneh\t250\tFinland\tHelsinki")


radius = 10
area = 3.14 * radius**2
print(f"The area of a circle with radius {radius} is ${area} meters square.")

"""
使用字符串格式化方法输出以下内容:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144
"""

a = 8
b = 6

# 输出加法
print(f"{a} + {b} = {a + b}")
# 输出减法
print(f"{a} - {b} = {a - b}")
# 输出乘法
print(f"{a} * {b} = {a * b}")
# 输出除法
print(f"{a} / {b} = {a / b:.2f}")  # 保留两位小数
# 输出取余
print(f"{a} % {b} = {a % b}")
# 输出整除
print(f"{a} // {b} = {a // b}")
# 输出幂运算
print(f"{a} ** {b} = {a ** b}")
