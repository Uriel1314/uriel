# 练习 7-3 10 的整数倍
# 让用户输入一个数，并指出这个数是否是 10 的整数倍。
number = input("Give me a number, please: ")
number = int(number)

if number % 10 == 0:
 print(f"{number} is a multiple of 10.")
else:
 print(f"{number} is not a multiple of 10.")