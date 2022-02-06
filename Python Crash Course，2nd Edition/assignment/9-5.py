"""
练习 9-5 尝试登录次数
在为完成练习 9-3 而编写的 User 类中，添加一个名为 login_attempts 的属性。编写
一个名为 increment_login_attempts() 的方法，它将属性 login_attempts 的值加 1。再编
写一个名为 reset_login_attempts() 的方法，它将属性 login_attempts 的值重置为 0。
根据 User 类创建一个实例，再调用方法 increment_login_attempts() 多次。打印属
性 login_attempts 的值，确认它被正确地递增；然后，调用方法 reset_login_attempts() ，
并再次打印属性 login_attempts 的值，确认它被重置为 0。
"""

class User():
	"""一个表示用户的简单类。"""

	def __init__(self, first_name, last_name, username, email, location):
		"""初始化用户."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
		self.login_attempts = 0

	def describe_user(self):
		"""显示用户信息摘要。"""
		print(f"\n{self.first_name} {self.last_name}")
		print(f" Username: {self.username}")
		print(f" Email: {self.email}")
		print(f" Location: {self.location}")


	def greet_user(self):
		"""向用户发出个性化问候。"""
		print(f"\nWelcome back, {self.username}!")

	def increment_login_attempts(self):
		"""将属性 login_attempts 的值加 1。"""
		self.login_attempts += 1

	def reset_login_attempts(self):
		"""将 login_attempts 重置为 0。"""
		self.login_attempts = 0


eric = User('eric', 'matthes', 'e_matthes', 'e_matthes@example.com', 'alaska')
eric.describe_user()
eric.greet_user()
		
print("\nMaking 3 login attempts...")
eric.increment_login_attempts()
eric.increment_login_attempts()
eric.increment_login_attempts()
print(f" Login attempts: {eric.login_attempts}")

print("Resetting login attempts...")
eric.reset_login_attempts()
print(f" Login attempts: {eric.login_attempts}")
