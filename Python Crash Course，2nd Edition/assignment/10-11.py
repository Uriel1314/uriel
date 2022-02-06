# 练习 10-11 喜欢的数
# 编写一个程序，提示用户输入他喜欢的数，并使用 json.dump() 将这个数字存储到文
# 件中。再编写一个程序，从文件中读取这个值，并打印消息“I know your favorite number! It’s
# _____.”。

import json

number = input("What's your favorite number? ")

with open('favorite_number.json', 'w') as f:
	json.dump(number, f)
	print("Thanks! I'll remember that.")


with open('favorite_number.json', 'r') as f:
	number = json.load(f)

print(f"I know you favorite number is {number}.")