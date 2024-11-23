"""
Write a function which count number of lines and number of words in a text.
All the files are in the data the folder:
a) Read obama_speech.txt file and count number of lines and words
b) Read michelle_obama_speech.txt file and count number of lines and words
c) Read donald_speech.txt file and count number of lines and words
d) Read melina_trump_speech.txt file and count number of lines and words
"""


# 读取obama_speech.txt 文件
file = open("../data/obama_speech.txt", "r", encoding="utf-8")
file_txt = file.read()
print(type(file_txt))

# 统计行数和单词数量

line_count = 0
word_count = 0

for line in file_txt.splitlines():
    line_count += 1

    # 按空格分割每行的单词，去除空白字符后统计
    words_in_line = line.split()
    word_count += len(words_in_line)

# 输出结果
print("Total number of lines:", line_count)
print("Total number of words:", word_count)

# 读取 michelle_obama_speech.txt
with open('../data/michelle_obama_speech.txt', 'r', encoding="utf-8") as file:
    line_count = 0
    word_count = 0
    # 使用 enumerate 获取行号和内容
    for line_number, line in enumerate(file, 1):  # 从 1 开始计数
        # 统计行数
        line_count += 1

        # 统计每行的单词数
        word_count += len(line.split())

# 输出结果
print(f"Total number of lines: {line_count}")
print(f"Total number of words: {word_count}")

# 读取 donald_speech.txt
with open('../data/donald_speech.txt', 'r', encoding="utf-8") as file:
    lines = file.readlines()
    # 统计行数
    line_count = len(lines)

    word_count = sum(map(lambda line: len(line.split()), lines))

# 输出结果
print(f"Total number of lines: {line_count}")
print(f"Total number of words: {word_count}")

"""
Extract all incoming email addresses as a list from the email_exchange_big.txt file.
"""
import re

email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
# 存储提取的电子邮件地址
email_addresses = []
with open('../data/email_exchanges_big.txt', 'r', encoding="utf-8") as file:
    for line in file:
        # 在每一行中查找所有匹配的电子邮件地址
        emails_in_line = re.findall(email_pattern, line)

        # 将找到的电子邮件地址添加到列表中
        email_addresses.extend(emails_in_line)

# Output the result
print(email_addresses)

"""
Find the most common words in the English language. 
Call the name of your function find_most_common_words, it will take two parameters 
- a string or a file and a positive integer, indicating the number of words. 
Your function will return an array of tuples in descending order. Check the output

    # Your output should look like this
    print(find_most_common_words('sample.txt', 10))
    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and'),
    (4, 'a'),
    (4, 'in'),
    (3, 'that'),
    (2, 'have'),
    (2, 'I')]

    # Your output should look like this
    print(find_most_common_words('sample.txt', 5))

    [(10, 'the'),
    (8, 'be'),
    (6, 'to'),
    (6, 'of'),
    (5, 'and')]
"""

# Reading the input: The input can either be a string or a file path. We need to handle both cases.
# Tokenizing the text: We will split the text into words using regular expressions, considering that words may include punctuation.
# Counting word frequencies: Use Python’s collections.Counter to efficiently count the frequency of each word.
# Sorting the results: Sort the words by their frequency in descending order.
# Returning the result: Return the top n most common words.

from collections import Counter


def find_most_common_words(input_data, n):
    # input_data 有可能是字符串或者文件
    if isinstance(input_data, str) and input_data.endswith(".txt"):
        with open(input_data, "r", encoding="utf-8") as file:
            text = file.read()
    else:
        text = input_data
    words = re.findall(r'\b\w+\b', text.lower())  # 转换为小写进行统计
    word_counts = Counter(words)
    most_common_words = word_counts.most_common(n)

    return most_common_words


text = """In a house in a house there was a dog. The dog ran around the house."""
top_words = find_most_common_words(text, 3)
print(top_words)

"""
Use the function, find_most_frequent_words to find: 
a) The ten most frequent words used in Obama's speech 
b) The ten most frequent words used in Michelle's speech 
"""
top_words = find_most_common_words("../data/donald_speech.txt", 10)
print(top_words)

"""
Write a python application that checks similarity between two texts. 
It takes a file or a string as a parameter and it will evaluate the similarity of the two texts. 
For instance check the similarity between the transcripts of Michelle's and Melina's speech. 
You may need a couple of functions, function to clean the text(clean_text), function to remove support words(remove_support_words) and finally to check the similarity(check_text_similarity). 
List of stop words are in the data directory
"""

from data.stop_words import stop_words
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    """
    清洗文本
    - 转换成小写
    - 去除非字母的单词
    """
    # Convert to lowercase
    text = text.lower()

    # 删除文本中所有 非小写字母 和 非空白字符（比如数字、标点符号等）。
    # 只保留文本中的小写字母和空白字符（空格、制表符等）。
    text = re.sub(r'[^a-z\s]', '', text)

    return text


def remove_support_words(text):
    """
    删除停用词
    """
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)


def load_text(file_path):
    """
    加载文件内容
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Function to check text similarity
def check_text_similarity(text1, text2):
    """
    Checks the similarity between two texts using cosine similarity.
    """
    # Clean and remove stop words from both texts
    cleaned_text1 = clean_text(text1)
    cleaned_text2 = clean_text(text2)

    cleaned_text1 = remove_support_words(cleaned_text1)
    cleaned_text2 = remove_support_words(cleaned_text2)

    # Vectorize the cleaned texts
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform([cleaned_text1, cleaned_text2])

    # Calculate the cosine similarity
    cosine_sim = cosine_similarity(vectors[0], vectors[1])

    return cosine_sim[0][0]

text1 = load_text('../data/michelle_obama_speech.txt')
text2 = load_text('../data/donald_speech.txt')

# Calculate similarity
similarity = check_text_similarity(text1, text2)
print(f"Text similarity: {similarity:.4f}")

"""
Find the 10 most repeated words in the romeo_and_juliet.txt

"""

"""
Read the hacker news csv file and find out: a) Count the number of lines containing python or Python b) Count the number lines containing JavaScript, javascript or Javascript c) Count the number lines containing Java and not JavaScript
"""
