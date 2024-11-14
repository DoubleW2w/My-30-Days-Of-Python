"""
第二天： 30 Days of python programming - level1
"""

import math


first_name = "Lin"
last_name = "Yh"
full_name = "LinYh"
country = "China"
city = "NanJing"
age = 27
year = 1997
is_married = False
is_true = True
is_light_on = True
phone_number, id_card = "1111", "2222"


"""
第二天： 30 Days of python programming - level2
"""
# 使用 type() 内置函数检查你声明变量的数据类型
print(type(is_married))

print(len(first_name))

# 比较你 first name 和 last name 变量的长度
print(len(first_name) > len(last_name))

# 声明变量 num_one 为5，num_two 为4
num_one, num_two = 5, 4
# 将 num_one 和 num_two 相加，并赋值给 total 变量
total = num_one + num_two

# 将 num_one 和 num_two 相减，并赋值给 diff 变量
diff = num_one - num_two

# 将 num_one 和 num_two 相乘，并赋值给 product 变量
product = num_one * num_two

# 将 num_one 和 num_two 相除，并赋值给 division 变量
division = num_one / num_two

# 使用模数除法求出 num_two 除以 num_one 的结果，并将结果赋给变量 remainder
remainder = num_two % num_one

# 计算 num_one 的 num_two 次方并将值赋给变量 exp
exp = num_one**num_two
# 计算 num_one 除以 num_two 商的整数部分（整除操作），并将结果赋给变量 floor_division
floor_division = num_one // num_two

# 计算圆的面积并将值赋给名为 area_of_circle 的变量
area_of_circle = math.pi * 30**2

# 计算圆的周长并将值赋给名为 circum_of_circle 的变量
circum_of_circle = 2 * math.pi * 30
# 将半径作为用户输入并计算面积。
# 获取用户输入的半径
radius = float(input("请输入圆的半径: "))
area_of_circle = math.pi * radius**2
# 输出计算结果
print(f"圆的面积为: {area_of_circle}")

# 在 Python shell 或文件中运行 help('keywords') 检查 Python 保留字或关键字
print(help("keywords"))
