"""
练习 9-9 电瓶升级
在本节最后一个electric_car.py版本中，给 Battery 类添加一个名为 upgrade_battery()
的方法。这个方法检查电瓶容量，如果它不是 85，就将它设置为 85。创建一辆电瓶容量为
默认值的电动汽车，调用方法 get_range() ，然后对电瓶进行升级，并再次调用
get_range() 。你将看到这辆汽车的续航里程增加了。
"""


class Car():
	"""一次模拟汽车的简单尝试。"""
	def __init__(self, manufacturer, model, year):
		"""初始化描述汽车的属性。"""
		self.manufacturer = manufacturer
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""返回整洁的描述性信息。"""
		long_name = f"{self.year} {self.manufacturer} {self.model}"
		return long_name.title()


	def read_odometer(self):
		"""打印一条指出汽车里程的消息。"""
		print(f"This car has {self.odometer_reading} miles on it.")


	def update_odometer(self, mileage):
		"""
		将里程表读数设置为指定的值。
		禁止将里程表读数往回调。
		"""
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")


	def increment_odometer(self, miles):
		"""将里程表读数增加指定的量。"""
		self.odometer_reading += miles


class Battery():
	"""一次模拟电动汽车电瓶的简单尝试。"""
	def __init__(self, battery_size=75):
		"""初始化电瓶的属性。"""
		self.battery_size = battery_size

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息。"""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""打印一条消息，指出电瓶的续航里程。"""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315


		message = f"This car can go approximately {range}"
		message += " miles on a full charge."
		print(message)

	def upgrade_battery(self):
		"""在可能的情况下将电瓶升级。"""
		if self.battery_size == 75:
			self.battery_size = 100
			print("Upgraded the battery to 100 kWh.")
		else:
			print("The battery is already upgraded.")


class ElectricCar(Car):
	"""电动汽车的独特之处。"""
	def __init__(self, manufacturer, model, year):
		"""
		初始化父类的属性。
		再初始化电动汽车特有的属性。
		"""
		super().__init__(manufacturer, model, year)
		self.battery = Battery()

print("Make an electric car, and check the battery:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.describe_battery()

print("\nUpgrade the battery, and check it again:")
my_tesla.battery.upgrade_battery()