from collections import Counter
from functools import reduce
from itertools import chain

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for item in countries:
    print(f"Country: {item}")
for i, name in enumerate(names):
    print(f"i: {i}, name: {name}")
for number in numbers:
    print(f"number: {number}")
print("---------------------------------------------")


# 使用 map 将 countries 列表中的每个国家更改为大写，生成一个新列表。
def countries_upper(x: str) -> str:
    return x.upper()


new_countries = map(countries_upper, countries)
print(list(new_countries))

# 使用 map 将 numbers 列表中的每个数字更改为平方，生成一个新列表。
x = lambda num: num * num
new_numbers = list(map(x, numbers))
print(new_numbers)

# 使用 map 将 names 列表中的每个名称更改为大写，生成一个新列表。
# 使用 filter 过滤出包含“land”的国家。
print(list(filter(lambda item: "land" in item, countries)))


# 声明一个函数 get_string_lists，它接收一个列表作为参数并返回一个仅包含字符串项的列表。
def get_string_lists(lst: list) -> list:
    return list(filter(lambda item: isinstance(item, str), lst))


test_list = ["test", 1, "mmm", 2]
print(get_string_lists(test_list))


# 使用 reduce 对 numbers 列表中的所有数字求和。
def add_two_nums(x, y):
    return int(x) + int(y)


print(reduce(lambda x, y: x + y, numbers))

# 使用 reduce 将所有国家连接起来，生成句子：Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries。
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']


# 定义连接国家的函数
def concatenate(acc, country):
    return acc + ', ' + country


# 使用 reduce 来连接国家名称
sentence = reduce(concatenate, countries)

# 将最后一个逗号替换为 "and"
sentence = sentence.rsplit(', ', 1)  # 从右边分割一次，得到最后两个部分
sentence = ' and '.join(sentence)  # 将最后两个部分用 ' and ' 连接

# 添加最终的国家描述
sentence = sentence + ' are north European countries.'
print(sentence)

from data.countries import countries as ct


# 声明一个 get_first_ten_countries 函数 - 它返回数据文件夹中 countries.js 列表中的前十个国家。
def get_first_ten_countries(lst: list) -> list:
    return lst[:10]


print(get_first_ten_countries(ct))


# 声明一个 get_last_ten_countries 函数 - 它返回国家列表中的最后十个国家。
def get_first_ten_countries(lst: list) -> list:
    return lst[-10:]


print(get_first_ten_countries(ct))


# 创建一个返回字典的函数，其中键表示国家名称的首字母，值表示以该字母开头的国家数。
def country_initial_count(countries):
    # 创建一个空字典来存储首字母和出现次数
    initial_count = {}

    # 遍历每个国家名称
    for country in countries:
        # 获取国家名称的首字母并转为大写（为了统一处理）
        initial = country[0].upper()

        # 如果该首字母已在字典中，计数加1，否则初始化为1
        if initial in initial_count:
            initial_count[initial] += 1
        else:
            initial_count[initial] = 1

    return initial_count


print(country_initial_count(ct))

from data.countries_data import list as ct_data_list

# 按照 'name'、'capital' 和 'population' 排序
sorted_countries = sorted(ct_data_list, key=lambda x: (x["name"], x["capital"], x["population"]))
print(sorted_countries)
print("------------------------------------------------------------")

# 按位置排序出前十个最常用语言。
all_languages = []
for item in ct_data_list:
    all_languages.extend(item["languages"])
print("------------------------------------------------------------")

# all_languages = list(chain(*map(lambda country: country["languages"], ct_data_list)))
# Step 2: 使用 Counter 统计语言出现次数
language_counts = Counter(all_languages)
print(language_counts)
# Step 3: 按出现次数排序并提取前十个语言
top_10_languages = language_counts.most_common(10)
print(top_10_languages)
# 输出前十个最常用的语言
for language, count in top_10_languages:
    print(f"Language: {language}, Count: {count}")

print("------------------------------------------------------------")
# 排序出前十个人口最多的国家。
# Step 1: 使用 sorted 按照人口从大到小排序
sorted_countries = sorted(ct_data_list, key=lambda x: x["population"], reverse=True)

# Step 2: 提取前十个国家
top_10_countries = sorted_countries[:10]
# Step 3: 输出前十个人口最多的国家
for country in top_10_countries:
    print(f"{country['name']} - Population: {country['population']}")
