# 练习 6-9 喜欢的地方
# 创建一个名为 favorite_places 的字典。在这个字典中，将三个人的名字用作键；对
# 于其中的每个人，都存储他喜欢的 1~3 个地方。为让这个练习更有趣些，让一些朋友指出
# 他们喜欢的几个地方。遍历这个字典，并将其中每个人的名字及其喜欢的地方打印出来。

favorite_places = {
 'eric': ['bear mountain', 'death valley', 'tierra del fuego'],
 'erin': ['hawaii', 'iceland'],
 'willie': ['mt. verstovia', 'the playground', 'new hampshire']
 }
for name, places in favorite_places.items():
	print(f"\n{name.title()} likes the following places:")
	for place in places:
		print(f"- {place.title()}")
