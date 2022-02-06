'''
练习 10-4 访客名单
编写一个 while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印问候
语，并将一条到访记录添加到文件 guest_book.txt 中。确保这个文件中的每条记录都独占一
行。
'''
filename = 'guest_book.txt'

print("Enter 'quit' when you are finished. ")
while True:
	name = input("What's your name? ")
	if name == 'quit':
		break
	else:
		with open(filename, 'a') as f:
			f.write(f"{name.title()}\n")
		print(f"Hi {name.title()}, you've been added to the guest book.")

		