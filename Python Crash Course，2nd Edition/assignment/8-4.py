"""
练习 8-4 大号 T 恤
修改函数 make_shirt() ，使其在默认情况下制作一件印有 “I love Python” 字样的
大号 T 恤。调用这个函数来制作如下 T 恤：一件印有默认字样的大号 T 恤、一件印有默认
字样的中号 T 恤、一件印有其他字样的 T 恤（尺码无关紧要）。
"""

def make_shirt(size='large', message='I love Python!'):
	"""概述要制作的 T 恤什么样。"""
	print(f"\nI'm going to make a {size} t-shirt.")
	print(f'It will say, "{message}"')


make_shirt()
make_shirt(size='medium')
make_shirt('small', 'Programmers are loopy.')