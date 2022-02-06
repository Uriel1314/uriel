'''
练习 8-3 T 恤
编写一个名为 make_shirt() 的函数，它接受尺码以及要印到 T 恤上的字样。这个函
数应打印一个句子，概要地说明 T 恤衫的尺码和字样。
使用位置实参调用这个函数来制作一件 T 恤，再使用关键字实参来调用这个函数。
'''

def make_shirt(size, message):
	"""概述要制作的 T 恤什么样。"""
	print(f"\nI'm going to make a {size} t-shirt.")
	print(f'It will say, "{message}"')


make_shirt('large', 'I love Python!')
make_shirt(message="Readability counts.", size='medium')

