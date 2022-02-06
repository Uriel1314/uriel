'''
练习 6-7 人们
在为完成练习 6-1 而编写的程序中，再创建两个表示人的字典，然后将这三个字典都
存储在一个名为 people 的列表中。遍历这个列表，将其中每个人的所有信息都打印出来。
'''

# 创建一个用于存储人的空列表。
people = []

# 定义一些人并将他们添加到前述列表中。
person = {
 'first_name': 'eric',
 'last_name': 'matthes',
 'age': 46,
 'city': 'sitka',
 }
people.append(person)

person = {
 'first_name': 'lemmy',
 'last_name': 'matthes',
 'age': 2,
 'city': 'sitka',
 }
people.append(person)
person = {
 'first_name': 'willie',
 'last_name': 'matthes',
 'age': 11,
 'city': 'sitka',
 }
people.append(person)

# 显示列表包含的每个字典中的信息。
for person in people:
 name = f"{person['first_name'].title()} {person['last_name'].title()}"
 age = person['age']
 city = person['city'].title()
 
 print(f"{name}, of {city}, is {age} years old.")