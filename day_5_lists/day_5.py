list_1 = []

list_2 = ["I", "Love", "U", "L", "S"]

len_1 = len(list_1)
len_2 = len(list_2)

first_item_in_list_2 = list_2[0]
middle_item_in_list_2 = list_2[len_2 // 2]
last_item_in_list_2 = list_2[len_2 - 1]

mixed_data_type = ["Lyh", 27, 1.66, False, "NanJing"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle"]

print(f"mixed_data_type: {mixed_data_type}")
print(f"len:{len(it_companies)}")
print(f"first item in it_companies: {it_companies[0]}")
print(f"middle item in it_companies: {it_companies[len(it_companies) // 2]}")
print(f"last item in it_companies: {it_companies[-1]}")

# 修改其中一家公司的名称后打印列表
it_companies[0] = "NANANNN"
print(f"it_companies: {it_companies}")

# 向 it_companies 添加一家 IT 公司
it_companies.append("yyyyy")
print(f"it_companies: {it_companies}")

# 在公司列表中间插入一家 IT 公司
it_companies.insert(2, "11111")

# 将其中一家 it_companies 公司的名称更改为大写（不包括 IBM!）
for company in it_companies:
    if company != "IBM":
        company = company.upper()

# 使用字符串 '#;  ' 连接 it_companies
result = "#;  ".join(it_companies)
print(f"使用字符串 '#;  '{result}")

# 检查 it_companies 列表中是否存在某个公司。
print(f"google 是否在列表中", "Google" in it_companies)

# 使用 sort() 方法对列表进行排序
it_companies.sort()
print(it_companies)

# 使用 reverse() 方法按降序反转列表
it_companies.reverse()
print(it_companies)

# 从列表中切分出前 3 家公司
print(it_companies[:3])

# 从列表中切分出最后 3 家公司
print(it_companies[-3:])

# 从列表中删除第一家 IT 公司
del it_companies[0]
print(it_companies)

# 从列表中删除中间的 IT 公司或公司
del it_companies[len(it_companies) // 2]

# 从列表中删除所有 IT 公司
it_companies.clear()

# 销毁 it_companies 列表
del it_companies

front_end = ["HTML", "CSS", "JS", "React", "Redux"]
back_end = ["Node", "Express", "MongoDB"]
# 在连接的列表中插入 Python 和 SQL 到变量 full_stack 之后。
full_stack = front_end + back_end
full_stack.append("Python")
full_stack.append("SQL")
print(f"full_stack: {full_stack}")

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

#  对列表进行排序，并找出最大和最小年龄
ages.sort()
max_age = ages[-1]
min_age = ages[0]
print(f"max_age:{max_age}")
print(f"min_age:{min_age}")

# 将最小年龄和最大年龄再次添加到列表中
ages.append(max_age)
ages.insert(0, min_age)

# 找到年龄中位数（一个中间项或两个中间项除以二）
# 获取列表长度
n = len(ages)
if n % 2 == 1:  # 如果是奇数，直接取中间的元素
    median = ages[n // 2]
else:  # 如果是偶数，取中间两个元素的平均值
    median = (ages[n // 2 - 1] + ages[n // 2]) / 2

print("Median:", median)

# 找到平均年龄（所有项的总和除以它们的数量）
# 计算总和
total_age = sum(ages)
# 计算平均年龄
average_age = total_age / n
print("Average age:", average_age)

# 找到年龄范围（最大减去最小）
# 计算最大值和最小值
max_age = max(ages)
min_age = min(ages)

# 计算年龄范围
age_range = max_age - min_age

print("Age range:", age_range)

# 比较 (min - average) 和 (max - average) 的值，使用 abs() 方法

# 计算 (min - average) 和 (max - average) 的绝对值
min_diff = abs(min_age - average_age)
max_diff = abs(max_age - average_age)


# 比较哪个更大
if min_diff > max_diff:
    print("min")
elif min_diff < max_diff:
    print("max")
else:
    print("equal")
