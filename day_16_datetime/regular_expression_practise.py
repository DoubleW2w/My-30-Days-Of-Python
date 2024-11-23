import re

"""
编写一个模式来识别字符串是否为有效的 python 变量
is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True
"""

valid_pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"


def is_valid_variable(s: str) -> bool:
    return bool(re.match(valid_pattern, s))


# 测试用例
test_cases = ["variable", "_var", "2variable", "class", "my_var_1", "with space", "11"]
results = {case: is_valid_variable(case) for case in test_cases}
print(results)

"""
清理以下文本。清理后，计算字符串中最常见的三个单词
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
"""


def clean_text(text):
    # 移除特殊字符，只保留字母、数字和空格
    cleaned = re.sub(r'[^\w\s]', '', text)
    return cleaned


def most_frequent_words(cleaned_text):
    # 分割单词并转换为小写
    words = cleaned_text.split()
    words = [word.lower() for word in words]

    # 手动统计单词频率
    word_freq = {}
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    # 按频率从高到低排序，取前三个单词
    sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_words[:3]


sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
# 清理文本
cleaned_text = clean_text(sentence)
print(cleaned_text)

# 找到最常见的三个单词
top_words = most_frequent_words(cleaned_text)
print(top_words)
