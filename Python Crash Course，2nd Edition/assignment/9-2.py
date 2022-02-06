"""
根据你为完成练习 9-1 而编写类创建三个实例，并对每个实例调用方法
describe_restaurant() 。
"""

class Restaurant():
	"""一个表示餐馆的类。"""

	def __init__(self, name, cuisine_type):
		"""初始化餐馆。"""
		self.name = name.title()
		self.cuisine_type = cuisine_type
	
	def describe_restaurant(self):
		"""显示餐馆信息摘要概述。"""
		msg = f"{self.name} serves wonderful {self.cuisine_type}."
		print(f"\n{msg}")
	
	def open_restaurant(self):
		"""显示一条消息，指出餐馆正在营业。"""
		msg = f"{self.name} is open. Come on in!"
		print(f"\n{msg}")


mean_queen = Restaurant('the mean queen', 'pizza')
mean_queen.describe_restaurant()


ludvigs = Restaurant("ludvig's bistro", 'seafood')
ludvigs.describe_restaurant()


mango_thai = Restaurant('mango thai', 'thai food')
mango_thai.describe_restaurant()