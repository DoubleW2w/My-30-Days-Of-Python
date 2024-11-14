"""
练习： 1级
创建一个空元组
创建一个包含你姐妹和兄弟名字的元组（虚构的兄弟姐妹也可以）
连接兄弟姐妹元组并将其分配给 siblings
你有多少兄弟姐妹？
修改兄弟姐妹元组并添加你父母的名字，然后将其分配给 family_members
练习： 2级
从 family_members 中获取兄弟姐妹和父母
创建 fruits、vegetables 和 animal products 元组。连接三个元组并将其分配给名为 food_stuff_tp 的变量。
将 food_stuff_tp 元组更改为 food_stuff_lt 列表
从 food_stuff_tp 元组或 food_stuff_lt 列表中切出中间项或项。
从 food_staff_lt 列表中切出前三项和最后三项
完全删除 food_staff_tp 元组
检查元组中是否存在项：
检查 'Estonia' 是否在 nordic_country 元组中

检查 'Iceland' 是否在 nordic_country 元组中
"""

tuple = tuple()

tuple_family_1 = ("Lsy", "Lyl")

tuple_family_2 = ("111", 222)

tuple_all = tuple_family_2 + tuple_family_1

print(f"我有多少个兄弟姐妹：{len(tuple_all)}")

# 添加父母名字
tuple_family_2 = ("Luo Ma", "Luo Pa")  # 假设父母名字是 'Luo Ma' 和 'Luo Pa'

# 合并父母和兄弟姐妹的元组
family_members = tuple_family_2 + tuple_family_1
# 输出家庭成员数量
print(f"我有多少个家庭成员：{len(family_members)}")

# 打印家庭成员的名字
print(f"我的家庭成员有：{family_members}")

fruits= ("banana", "apple")
vegetables= ("banana", "apple")
animal= ("banana", "apple")

food_stuff_tp = fruits + vegetables + animal + animal
food_stuff_lt = list(food_stuff_tp)
# 从元组中切出中间项（以元组的长度为例）
middle_index = len(food_stuff_tp) // 2  # 获取中间项的索引
middle_item_tp = food_stuff_tp[middle_index]  # 获取中间项
print(f"food_stuff_tp 中间项: {middle_item_tp}")
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
del food_stuff_tp

# 定义 nordic_country 元组
nordic_country = ("Denmark", "Finland", "Iceland", "Norway", "Sweden")

is_estonia_in_nordic = 'Estonia' in nordic_country
print("Is Estonia in nordic_country?", is_estonia_in_nordic)

is_iceland_in_nordic = 'Iceland' in nordic_country
print("Is Iceland in nordic_country?", is_iceland_in_nordic)
