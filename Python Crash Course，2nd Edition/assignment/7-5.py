'''
练习 7-5 电影票
有家电影院根据观众的年龄收取不同的票价：不到 3 岁的观众免费；3~12 岁的观众为
10 美元；超过 12 岁的观众为 15 美元。请编写一个循环，在其中询问用户的年龄，并指出
其票价。
'''

prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "
while True:
	age = input(prompt)
	if age == 'quit':
		break
	age = int(age)
	
	if age < 3:
 		print(" You get in free!")
	elif age < 13:
		print(" Your ticket is $10.")
	else:
		print(" Your ticket is $15.")
