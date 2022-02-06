'''
在你为完成练习 4-1 而编写的程序中，创建比萨列表的副本，并将其存储到变量
friend_pizzas 中，再完成如下任务：
 在原来的比萨列表中添加一种比萨。
 在列表 friend_pizzas 中添加另一种比萨。
 核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一
个 for 循环打印第一个列表；打印消息“My friend’s favorite pizzas are:”，再使用
一个 for 循环打印第二个列表。核实新增的比萨被添加到正确的列表中。
'''

favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append("meat lover's")
friend_pizzas.append("pesto")

print("My favorite pizzas are: ")
for pizza in favorite_pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are: ")
for pizza in friend_pizzas:
	print(pizza)