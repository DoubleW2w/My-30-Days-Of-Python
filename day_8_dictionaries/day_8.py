"""
创建一个名为 dog 的空字典
向 dog 字典添加 name、color、breed、legs、age 键
创建一个学生字典，添加 first_name、last_name、gender、age、marital status、skills、country、city 和 address 作为字典的键
获取学生字典的长度
获取 skills 的值并检查数据类型，应该是列表
修改 skills 值，添加一到两个技能
获取字典的键列表
获取字典的值列表
使用 items() 方法将字典变为由元组组成的列表
删除字典中的一项
删除其中一个字典
"""

dog = dict()
dog['name'] = '111'
dog['color'] = 'red'
dog['breed'] = '11'
dog['leg'] = 4
dog['age'] = 22

student_dic = {}
student_dic['first_name'] = '2323'
student_dic['last_name'] = '12312343'
student_dic['gender'] = 'sss'
student_dic['age'] = 4
student_dic['marital'] = '12312'
student_dic['status'] = False
student_dic['skills'] = "112312"
student_dic['country'] = "asdad"
print(len(student_dic))
print(student_dic)
for value in student_dic.values():
    print(f"{value} type is {type(value)}")
print(type(student_dic.values()))

student_dic['skills']=12312
print(student_dic)
print(student_dic.keys())
print(student_dic.items())
