# 练习 6-10 喜欢的数 2
# 修改为完成练习 6-2 而编写的程序，让每个人都可以有多个喜欢的数，然后将每个人
# 的名字及其喜欢的数打印出来。

favorite_numbers = {
 'mandy': [42, 17],
 'micah': [42, 39, 56],
 'gus': [7, 12],
 }

for name, numbers in favorite_numbers.items():
	print(f"{name.title()} likes the following numbers:")
	for number in numbers:
		print(f"\t-{number}")