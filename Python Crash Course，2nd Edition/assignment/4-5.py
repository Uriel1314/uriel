"""
练习 4-5 一百万求和
创建一个包含数 1～1 000 000 的列表，再使用 min()和 max()核实该列表确实是从 1
开始、到 100000 结束的。另外，对这个列表调用函数 sum()，看看 Python 将一百万个数
相加需要多长时间。
"""

numbers = list(range(1, 1_000_001))
for number in numbers:
	print(number)
print(min(numbers))
print(max(numbers))
print(sum(numbers))
