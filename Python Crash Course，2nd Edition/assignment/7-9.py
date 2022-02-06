'''
练习 7-9 五香烟熏牛肉卖完了
使用为完成练习 7-8 而创建的列表 sandwich_orders ，并确保 'pastrami' 在其中至少
出现了三次。在程序开头附近添加这样的代码：打印一条消息，指出熟食店的五香烟熏牛
肉（pastrami）卖完了；再使用一个 while 循环将列表 sandwich_orders 中的 'pastrami'
都删除。确认最终的列表 finished_sandiches 中未包含 'pastrami' 。
'''

sandwich_orders = [
 'pastrami', 'veggie', 'grilled cheese', 'pastrami',
 'turkey', 'roast beef', 'pastrami']

finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')
print("\n")

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I'm working on your {current_sandwich} sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\n")

for sandwich in finished_sandwiches:
	print(f"I made a {sandwich} sandwich.")
