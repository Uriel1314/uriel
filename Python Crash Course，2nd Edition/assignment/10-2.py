"""
练习 10-2 C 语言学习笔记
你可使用方法 replace() 将字符串中的特定单词都替换为另一个单词。下面是一个简
单的示例，演示了如何将句子中的 'dog' 替换为 'cat' ：
"""

msg = 'I really like dogs.'
print(msg.replace('dog', 'cat'))
print(msg)

filename = 'learning_python.txt'
with open(filename) as f:
	lines = f.readlines()


for line in lines:
	# 删除行尾的换行符，再将 Python 替换为 C。
	line  = line.rstrip()
	print(line.replace('Python', 'C'))

	print(line.rstrip().replace('Python', 'Java'))
