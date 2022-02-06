"""
练习 9-14 彩票
创建一个列表或元组，其中包含 10 个数和 5 个字母。从这个列表或元组中随机地选
择 4 个数或字母，并打印一条消息，指出只要彩票上是这 4 个数或字母，就中大奖了。
"""

from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = []
print("Let's see what the winning ticket is...")

# 中奖组合中不能包含重复的数或字母，因此使用了 while 循环。
while len(winning_ticket) < 4:
	pulled_item = choice(possibilities)
	
	# 仅当摇出的数字或字母不在组合中时，才将其添加到组合中。
	if pulled_item not in winning_ticket:
		print(f" We pulled a {pulled_item}!")
		winning_ticket.append(pulled_item)