"""
练习 8-6 城市名
编写一个名为 city_country() 的函数，它接受城市的名称和所属的国家。这个函数应
返回一个格式类似于下面的字符串：
"Santiago, Chile"
至少使用三个城市-国家对调用这个函数，并打印返回的值。
"""


def city_country(city, country):
	"""返回一个类似于'Santiago, Chile'的字符串。"""
	return f"{city.title()}, {country.title()}"



city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
