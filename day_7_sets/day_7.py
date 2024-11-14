"""
练习：第 1 级
找到集合 it_companies 的长度
向 it_companies 添加'Twitter'
一次性向集合 it_companies 插入多个 IT 公司
从集合 it_companies 中移除一家公司
移除和丢弃之间有什么区别
练习：第 2 级
合并 A 和 B
找到 A 和 B 的交集
A 是 B 的子集吗
A 和 B 是不相交集合吗
将 A 与 B 合并，反之亦然
A 和 B 之间的对称差异是什么
完全删除集合
练习：第 3 级
将年龄转换为集合并比较列表和集合的长度，哪一个更大？
解释以下数据类型之间的区别：字符串、列表、元组和集合
我是一个老师，我喜欢激励和教导人们。 这句句子中用了多少独特的单词？使用 split 方法和集合来获取独特的单词。
"""
it_companies = {'item1', 'item2', 'item3', 'item4'}

it_companies.add("Twitter")
print(it_companies)
it_companies_2 = {"111", "2222"}
it_companies.update(it_companies_2)  # union
print(it_companies)

it_companies.remove("Twitter")

# remove() 方法用于从集合中移除指定的元素。如果元素不存在，则会引发 KeyError 异常。
# discard() 方法用于从集合中丢弃指定的元素。与 remove() 不同的是，如果元素不存在，它不会抛出异常。


a = {"I", "Us"}
b = {"I", "UPOI"}
d = {"I"}
c = a.union(b)
print(c)
print(a.intersection(b))
print(a.issubset(b))  # true :a是b的子集 false: a不是b的子集
print(len(a.difference(b)) == 0)  # true：a和b是不相交集合 false: a和b是相交集合
print(a.isdisjoint(b))
print(a.symmetric_difference(b))

# 字符串、列表、元组和集合的区别
"""
有序性：列表、元组、字符串是有序的，集合元素是无序
重复性：列表、元组、字符串是可重复，集合元素是唯一的
可变性：字符串、元组 不可变，列表和集合是可变的
元素类型：字符串是仅字符，列表是任意类型，元组是任意类型，集合是任意类型
"""
