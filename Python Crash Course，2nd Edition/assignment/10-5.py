# 练习 10-5 调查
# 编写一个 while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添
# 加到一个存储所有原因的文件中

filename = 'programming_poll.txt'

responses = []

while True:
	response = input("\nWhy do you like programming? ")
	responses.append(response)

	continue_poll = input("Would you like to let someone else respond? (y/n) ")
	if continue_poll != 'y':
		break

with open(filename, 'a') as f:
	for responses in responses:
		f.write(f"{response}\n")


with open(filename) as f:
	contents = f.read()
print(contents)