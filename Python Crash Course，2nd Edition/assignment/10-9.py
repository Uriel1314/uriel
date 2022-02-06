# 练习 10-9 静默的猫和狗
# 修改你在练习 10-8 中编写的 except 代码块，让程序在文件不存在时静默失败。


filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
	
	try:
		with open(filename) as f:
			contents = f.read()
			# print(contents)

	except FileNotFoundError:
		# print(" Sorry, I can't find that file.")
		pass
	else:
		print(f"\nReading file: {filename}")
		print(contents)