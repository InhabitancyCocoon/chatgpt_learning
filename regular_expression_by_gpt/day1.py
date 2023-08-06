import re
import string

f = open('day1.text', encoding='utf-8')
s = f.read()
print(s)


# Task1 识别所有大写字母开头的单词
pattern1 = r'\b[A-Z]\w*\b' 
res1 = re.findall(pattern1, s)
print(res1)


# Task2 识别大写字母开头，且字符个数不超过10，为了观察方便，改为6
pattern2 = r'\b[A-Z]\w{0,5}\b'
res2 = re.findall(pattern2, s)
print(res2)


# Task3 识别所有后缀标点符号的单词
pattern3 = r'\b\w+(?=[^\w\s])'
res3 = re.findall(pattern3, s)
print(res3)

# import re

# text = "This is a Sample Text, with several Capitalized Words!"
# pattern = r'\b\w+(?=\p{P})'
# words_with_punctuation = re.findall(pattern, text)

# print(words_with_punctuation)

# print(string.punctuation)