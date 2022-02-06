# 传递任意数量的形参
def make_pizza(size, *toppings):
	""" 打印顾客点的披萨 """
	# print(toppings)

	""" 概述要制作的披萨 """
	print(f"\nMaking a {size} pizza with the following toppings:")
	for topping in toppings:
		print(f"-{topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
