'''
练习 6-2 喜欢的数
使用一个字典来存储一些人喜欢的数。请想出 5 个人的名字，并将这些名字用作字典
中的键；想出每个人喜欢的一个数，并将这些数作为值存储在字典中。打印每个人的名字
和喜欢的数。为让这个程序更有趣，通过询问朋友确保数据是真实的。
'''

favorite_numbers = {
	 'mandy': 42,
	 'micah': 23,
	 'gus': 7,
	 'hank': 1000_000,
	 'maggie': 0,
 }

num = favorite_numbers['mandy']
print(f"Mandy's favorite number is {num}.")

num = favorite_numbers['micah']
print(f"Micah's favorite number is {num}.")

num = favorite_numbers['gus']
print(f"Gus's favorite number is {num}.")

num = favorite_numbers['hank']
print(f"Hank's favorite number is {num}.")

num = favorite_numbers['maggie']
print(f"Maggie's favorite number is {num}.")
