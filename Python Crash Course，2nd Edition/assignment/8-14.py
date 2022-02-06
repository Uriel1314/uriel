"""
练习 8-14 汽车
编写一个函数，将一辆汽车的信息存储在字典中。这个函数总是接受制造商和型号，
还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的信息，还有两个名称值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
car = make_car('subaru', 'outback', color='blue', tow_package=True)
"""

def make_car(manufacturer, model, **options):
	""" 创建一个表示汽车的字典 """
	car_dict = {
		'manufacturer': manufacturer.title(),
		'mode': model.title(),
		}

	for option, value in options.items():
		car_dict[option] = value

	return car_dict



car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
