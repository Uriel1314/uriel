"""
练习 9-13 骰子
模块 random 包含以各种方式生成随机数的函数，其中的 randint() 随机返回一个位
于指定范围内的整数，例如，下面的代码随机地返回一个 1~6 的整数：
from random import randint
x = randint(1, 6)
请创建一个 Die 类，它包含一个名为 sides 的属性，该属性的默认值为 6。编写一
个名为 roll_die() 的方法，它打印位于 1 和骰子面数之间的随机数。创建一个 6 面的骰子
再掷 10 次。
创建一个 10 面的骰子和一个 20 面的骰子，再分别掷 10 次。
"""
from random import randint

"""一个表示骰子的类。"""
class Die(object):
	"""docstring for Die"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		"""返回一个位于 1 和骰子面数之间的随机数。"""
		return randint(1, self.sides)

# 创建一个 6 面的骰子，再掷 10 次并显示结果。
d6 = Die()

results = []
for roll_num in range(10):
	result = d6.roll_die()
	results.append(result)

print("10 rolls of a 6-sided die:")
print(results)


# 创建一个 10 面的骰子，再掷 10 次并显示结果。
d10 = Die(sides=10)

results = []
for roll_num in range(10):
	result = d10.roll_die()
	results.append(result)

print("\n10 rolls of a 10-sided die:")
print(results)

# 创建一个 20 面的骰子，再掷 10 次并显示结果。
d20 = Die(sides=20)

results = []
for roll_num in range(10):
	result = d20.roll_die()
	results.append(result)

print("\n10 rolls of a 20-sided die:")
print(results)


