# 练习 10-10 常见单词
# 访问古登堡计划（http://gutenberg.org/），并找一些你想分析的图书。下载这些作品的
# 文本文件或将浏览器中的原始文本复制到文本文件中。
# 你可使用方法 count() 来确定特定的单词或短语在字符串中出现了多少次。例如，下
# 面的代码计算 'row' 在一个字符串中出现了多少次：
# >>> line = "Row, row, row your boat"
# >>> line.count('row')
# 2
# >>> line.lower().count('row')
# 3
# 请注意，通过使用 lower() 将字符串转换为小写，可捕捉要查找的单词的各种外观，
# 而不管其大小写格式如何。
# 编写一个程序，它读取你在古登堡计划中获取的文件，并计算单词'the'在每个文件
# 中分别出现了多少次。这里计算得到的结果并不准确，因为将诸如'then'和'there'等
# 单词也计算在内了。请尝试计算'the '（包含空格）出现的次数，看看结果相差多少。

def count_common_words(filename, word):
	"""计算指定的单词在图书中出现了多少次。"""
	# 请注意，这里计算得到的结果并不准确，比实际出现的次数要多。

	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		word_count = contents.lower().count(word)
		msg = f"'{word}' appears in {filename} about {word_count} times."
		print(msg)

filename = 'alice.txt'

count_common_words(filename, 'the')
