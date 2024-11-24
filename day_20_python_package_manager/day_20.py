"""
读取以下 URL 内容并找出出现频率最高的 10 个单词
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
"""

import requests, re, collections

romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
url = requests.get(romeo_and_juliet)
text = url.text

# 清理文本：移除标点符号并将所有字母转换为小写
text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
# 分词
words = text.split()

# 统计单词频率
word_counts = collections.Counter(words)
# 输出最常见的 10 个单词
most_common_words = word_counts.most_common(10)
print("The 10 most common words are:")
for word, count in most_common_words:
    print(f"{word}: {count}")
