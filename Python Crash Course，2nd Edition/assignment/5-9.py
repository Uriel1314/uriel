'''
练习 5-10 检查用户名
按下面说的编写一个程序，模拟网站确保每位用户的用户名都独一无二的方式。
 创建一个至少包含 5 个用户名的列表，并将其命名为 current_users 。
 再创建一个包含 5 个用户名的列表，将其命名为 new_users ，并确保其中有一两个用
户名也包含在列表 current_users 中。
 遍历列表 new_users ，对于其中的每个用户名，都检查它是否已被使用。如果是这样，
就打印一条消息，指出需要输入别的用户名；否则，打印一条消息，指出这个用户名
未被使用。
练习答案
·26·
 确保比较是区分大小写；换句话说，如果用户名 'John' 已被使用，应拒绝用户名
'JOHN' 。
'''

current_users = ['eric', 'willie', 'admin', 'erin', 'Ever']
new_users = ['sarah', 'Willie', 'PHIL', 'ever', 'Iona']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
	if new_user.lower() in current_users:
		print(f"Sorry {new_user}, that name is taken.")
	else:
		print(f"Great, {new_user} is still available")




