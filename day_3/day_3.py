"""
day_3： 30 Days of python programming
"""

# 声明一个值是你年龄的整型变量
import math

pi = math.pi

age = 27

# 声明一个值是你身高的浮点型变量
tall = 1.66

# 声明一个值是复数变量
location = 1 + 1j

# 编写一个脚本，提示用户输入三角形的底和高，并计算这个三角形的面积（面积 = 0.5 x b x h）。
# 输入底: 20,输入高: 10,三角形的面积是 100

bottom = float(input("输入底："))
height = float(input("输入高："))
area_of_third_angle = bottom * height * 0.5
print(f"三角形的面积是： {area_of_third_angle}")


# 编写一个脚本，提示用户输入三角形的边 a、边 b 和边 c。计算三角形的周长（周长 = a + b + c）。
# 输入边 a: 5,输入边 b: 4,输入边 c: 3,三角形的周长是 12
a = int(input("输入边 a："))
b = int(input("输入边 b："))
c = int(input("输入边 c："))
round = a + b + c
print(f"三角形的周长是  {round}")

# 提示用户输入矩形的长度和宽度。计算其面积（面积 = 长 x 宽）和周长（周长 = 2 x (长 + 宽)）
length = int(input("输入矩形长度："))
width = int(input("输入矩形宽度："))
area_of_rectangle = length * width
round_of_rectangle = 2 * (length + width)
print(f"矩形面积为  {area_of_rectangle}")
print(f"矩形周长为  {round_of_rectangle}")

# 提示用户输入圆的半径。计算面积（面积 = pi x r x r）和周长（周长 = 2 x pi x r），其中 pi = 3.14。
radius = float(input("输入圆的半径："))
area_of_circle = pi * radius**2
round_of_circle = 2 * pi * radius
print(f"圆的面积是： {area_of_circle}")
print(f"圆的周长是： {round_of_circle}")


# 计算 y = 2x -2 的斜率、x 截距和 y 截距
def calculate_line_properties():
    # 方程的系数
    m = 2  # 斜率
    b = -2  # y 截距

    # 计算 x 截距
    x_intercept = -b / m  # 当 y = 0 时，解得 x 截距

    return m, b, x_intercept


# 获取斜率、y 截距和 x 截距
slope, y_intercept, x_intercept = calculate_line_properties()

# 输出结果
print(f"斜率 (Slope): {slope}")
print(f"y 截距 (y-intercept): {y_intercept}")
print(f"x 截距 (x-intercept): {x_intercept}")


# 斜率是 (m = y2-y1/x2-x1)。找到点 (2, 2) 和点 (6,10) 之间的斜率和欧几里得距离。
# 给定的点
x1, y1 = 2, 2
x2, y2 = 6, 10

# 计算斜率
slope = (y2 - y1) / (x2 - x1)

# 计算欧几里得距离
distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# 输出结果
print(f"斜率 (Slope): {slope}")
print(f"欧几里得距离 (Euclidean Distance): {distance}")


# 计算 y 的值（y = x^2 + 6x + 9）。尝试使用不同的 x 值，并找出 y 何时为 0。
def calculate_y(x):
    return x**2 + 6 * x + 9


# 尝试不同的 x 值
x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
for x in x_values:
    y = calculate_y(x)
    print(f"When x = {x}, y = {y}")

    if y == 0:
        print(f"Found y = 0 when x = {x}")


# 求出 'python' 和 'dragon' 的长度，并进行一个假的比较语句。
len_str1 = len("python")
len_str2 = len("dragon")
# 假的比较语句：比较两个相等的长度是否不同
if len_str1 != len_str2:
    print("The lengths are different.")
else:
    print("This comparison is fake, since the lengths are actually the same.")


# 使用 and 运算符检查 'python' 和 'dragon' 中是否都有 'on'。
if "on" in "python" and "on" in "dragon":
    print("yes")
else:
    print("no")

print("jargon" in "I hope this course is not full of jargon。")


# I hope this course is not full of jargon。使用 in 运算符检查句子中是否有 jargon。
sentence = "I hope this course is not full of jargon."

if "jargon" in sentence:
    print("yes")
else:
    print("no")

#'dragon' 和 'python' 中都没有 'on'。
if "on" not in "dragon" and "on" not in "python":
    print("yes")
else:
    print("no")

# 找到文本 python 的长度，并将该值转换为浮点数，然后将其转换为字符串。
# 原始字符串
text = "python"

# 计算字符串的长度
length = len(text)

# 将长度转换为浮点数
length_float = float(length)

# 将浮点数转换为字符串
length_str = str(length_float)
# 输出结果
print(f"Length of the string '{text}' as float: {length_float}")
print(f"Length as string: {length_str}")
# 偶数可以被 2 整除，余数为零。如何使用 Python 检查一个数字是偶数还是奇数？

num = int(input("请输入一个数"))
if num % 2 == 0:
    print("偶数")
else:
    print("奇数")

# 检查 7 除以 3 的Floor除法是否等于 2.7 的整数转换值。
# 检查 '10' 的类型是否等于 10 的类型。
# 检查 int('9.8') 是否等于 10。
# 编写一个脚本，提示用户输入工时和时薪。计算用户的工资。
