''' 练习 4-8 立方
将同一个数乘三次称为立方。例如，在 Python 中，2 的立方用 2**3 表示。请创建一
个列表，其中包含前 10 个整数（即 1～10）的立方，再使用一个 for 循环将这些立方数
都打印出来。
'''
numbers = [number**3 for number in range(1, 11)]
for number in numbers:
	print(number, end="\t")
print() 

cubes = []
for number in range(1, 11):
	cube = number**3
	cubes.append(cube)

for cube in cubes:
	print(cube, end="\t")
print(f"\n{cubes}")

