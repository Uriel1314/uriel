"""
练习 9-4 就餐人数
在为完成练习 9-1 而编写的程序中，添加一个名为 number_served 的属性，并将其默
认值设置为 0。根据这个类创建一个名为 restaurant 的实例；打印有多少人在这家餐馆就
餐过，然后修改这个值并再次打印它。
添加一个名为 set_number_served() 的方法，它让你能够设置就餐人数。调用这个方
法并向它传递一个值，然后再次打印这个值。
添加一个名为 increment_number_served() 的方法，它让你能够增加就餐人数。调用
这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就餐人数。
"""

class Restaurant():
	"""一个表示餐馆的类。"""
	def __init__(self, name, cuisine_type):
		"""初始化餐馆。"""
		self.name = name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""显示餐馆信息摘要。"""
		msg = f"{self.name} serves wonderful {self.cuisine_type}."
		print(f"\n{msg}")

	def open_restaurant(self):
		"""显示一条消息，指出餐馆正在营业。"""
		msg = f"{self.name} is open. Come on in!"
		print(f"\n{msg}")

	def set_number_served(self, number_served):
		"""让用户能够设置就餐人数。"""
		self.number_served = number_served

	def increment_number_served(self, additional_served):
		"""让用户能够增加就餐人数。"""
		self.number_served += additional_served

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430

print(f"Number served: {restaurant.number_served}")
restaurant.set_number_served(1257)

print(f"Number served: {restaurant.number_served}")
restaurant.increment_number_served(239)

print(f"Number served: {restaurant.number_served}")