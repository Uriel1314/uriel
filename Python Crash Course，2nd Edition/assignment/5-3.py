'''
练习 5-3 外星人颜色
假设在游戏中刚射杀了一个外星人，请创建一个名为 alien_color 的变量，并将其设
置为 'green' 、 'yellow' 或 'red' 。
 编写一条 if 语句，检查外星人是否是绿色的；如果是，就打印一条消息，指出玩家
获得了 5 分。
 编写这个程序的两个版本，在一个版本中上述测试通过了，而在另一个版本中未通过
（未通过测试时没有输出）。
'''

alien_color = 'green'

if alien_color == 'green':
	print("You just earned 5 points.")

alien_color = 'red'
if alien_color == 'green':
 print("You just earned 5 points!")