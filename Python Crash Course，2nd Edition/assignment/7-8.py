# 练习 7-8 熟食店
# 创建一个名为 sandwich_orders 的列表，在其中包含各种三明治的名字；再创建一个
# 名为 finished_sandwiches 的空列表。遍历列表 sandwich_orders ，对于其中的每种三明
# 治，都打印一条消息，如 I made your tuna sandwich ，并将其移到列表 finished_sandwiches 。
# 所有三明治都制作好后，打印一条消息，将这些三明治列出来。


sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I'm working on your {current_sandwich} sandwich.")
	finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
	print(f"I made a {sandwich} sandwich.")