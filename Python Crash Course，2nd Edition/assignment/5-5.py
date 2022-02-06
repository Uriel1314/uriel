'''
练习 5-5 外星人颜色 3
将练习 5-4 中的 if-else 结构改为 if-elif-else 结构。
 如果外星人是绿色的，就打印一条消息，指出玩家获得了 5 分。
 如果外星人是黄色的，就打印一条消息，指出玩家获得了 10 分。
 如果外星人是红色的，就打印一条消息，指出玩家获得了 15 分。
 编写这个程序的三个版本，它们分别在外星人为绿色、黄色和红色时打印一条消息。
外星人为红色的版本：
'''

alien_color = 'red'
if alien_color == 'green':
	print("You just earned 5 points!")
elif alien_color == 'yellow':
	print("You just earned 10 points!")
else:
	print("You just earned 15 points!")

	