# 练习 8-12 三明治
# 编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个函数只有一个形参
# （它收集函数调用中提供的所有食材），并打印一条消息，对顾客点的三明治进行概述。调
# 用这个函数三次，每次都提供不同数量的实参。

def make_sandwich(*items):
	"""使用指定的食材制作三明治。"""
	print("\nI'll make you a great sandwich:")
	for item in items:
		print(f" ...adding {item} to your sandwich.")
	print("Your sandwich is ready!")


make_sandwich('roast beef', 'cheddar cheese', 'lettuce', 'honey dijon')
make_sandwich('turkey', 'apple slices', 'honey mustard')
make_sandwich('peanut butter', 'strawberry jam')
