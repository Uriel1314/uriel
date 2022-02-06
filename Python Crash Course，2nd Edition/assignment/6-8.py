'''
练习 6-8 宠物
创建多个字典，对于每个字典，都使用一个宠物的名称来给它命名；在每个字典中，
包含宠物的类型及其主人的名字。将这些字典存储在一个名为 pets 的列表中，再遍历该
列表，并将有关每个宠物的所有信息都打印出来。
注意：提供练习答案时，我才发现这个问题表述得不太完美。实际上，使用宠物的名
称给描述它的字典命名不合理，而应将宠物的名称包含在字典。下面的练习答案就是按这
里说的做的。
'''

# 创建一个用于存储宠物的空列表。
pets = []
# 定义各个宠物并将其存储到列表中。
pet = {
	'animal type': 'python',
	'name': 'john',
	'owner': 'guido',
	'weight': 43,
	'eats': 'bugs',
}
pets.append(pet)

pet = {
	'animal type': 'chicken',
	'name': 'clarence',
	'owner': 'tiffany',
	'weight': 2,
	'eats': 'seeds',
}
pets.append(pet)

pet = {
	'animal type': 'dog',
	'name': 'peso',
	'owner': 'eric',
	'weight': 37,
	'eats': 'shoes',
}
pets.append(pet)

print(pets)

# 显示每个宠物的信息。
for pet in pets:
	print(f"\nHere's what I know about {pet['name'].title()}:")
	
	for key, value in pet.items():
		print(f"\t{key}: {value}")
