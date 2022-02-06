'''
	练习 4-7 3 的倍数
创建一个列表，其中包含 3~30 能被 3 整除的数；再使用一个 for 循环将这个列表中
的数都打印出来。
'''

numbers = list(range(3, 31, 3))
print(numbers)
for number in numbers:
	print(number, end = "\t")
print() # newline

