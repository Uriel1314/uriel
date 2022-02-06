"""
练习 9-6 冰激凌小店
冰激凌小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的类，让它继承你为完
成练习 9-1 或 9-4 而编写的 Restaurant 类。这两个版本的 Restaurant 类都可以，挑选你
更喜欢的那个即可。添加一个名为 flavors 的属性，用于存储一个由各种口味的冰激凌组
成的列表。编写一个显示这些冰激凌的方法。创建一个 IceCreamStand 实例，并调用这个
方法。
"""

class Restaurant:
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

class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self, name, cuisine_type='ice_cream'):
		super().__init__(name, cuisine_type)
		self.flavors = []

	def show_flavors(self):
		"""显示出售的冰激凌品种。"""
		print("\nWe have the following flavors available:")
		for flavor in self.flavors:
			print(f"- {flavor.title()}")

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanilla', 'chocolate', 'black cherry']

big_one.describe_restaurant()
big_one.show_flavors()