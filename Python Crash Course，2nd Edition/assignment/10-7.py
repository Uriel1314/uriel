# 练习 10-7 加法计算器
# 将你为完成练习 10-6 而编写的代码放在一个 while 循环中，让用户犯错（输入的是
# 文本而不是数）后能够继续输入数。


print("Enter 'q' at any time to quit.\n")

while True:
	try:
		x = input("\nGive me a number: ")
		if x == 'q':
			break

		x = int(x)

		y = input("\nGive me another number: ")
		if y == 'q':
			break

		y = int(y)

	except ValueError:
		print("Sorry, I really needed a number.")
	
	else:
		sum = x + y
		print(f"The sum of {x} and {y} is {sum}.")