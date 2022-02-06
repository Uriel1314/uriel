'''
练习 4-13 自助餐
有一家自助式餐馆，只提供五种简单的食品。请想出五种简单的食品，并将其存储在
一个元组中。
 使用一个 for 循环将该餐馆提供的五种食品都打印出来。
 尝试修改其中的一个元素，核实 Python 确实会拒绝你这样做。
 餐馆调整了菜单，替换了它原来提供的两种食品。请编写一个这样的代码块：给元组
变量赋值，并使用一个 for 循环将新元组的每个元素都打印出来。
'''

menu_items = ('rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
 'salmon burger', 'crab cakes',)

print("You can chosse from the following menu items:")
for item in menu_items:
	print(f"- {item}")
print(id(menu_items))

menu_items = (
 'rockfish sandwich', 'halibut nuggets', 'smoked salmon chowder',
 'black cod tips', 'king crab legs',
 )

print("\nOur menu has been updated.")
print("You can now choose from the following items:")

for item in menu_items:
	print(f"- {item}")

print(id(menu_items))