# Traceback (most recent call last):
#   File "C:\Users\wjun1\Desktop\Python Crash Course，2nd Edition\chap10\division_calculator.py", line 1, in <module>
#     print(5/0)
# ZeroDivisionError: division by zero

try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

print("Give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = int(input("\nFirst numebr: "))
	if first_number == 'q':
		break
	second_number = int(input("\nSecond number: "))
	if second_number == 'q':
		break

	try:
		answer = first_number / second_number
	except ZeroDivisionError:
		print("You can't divide by zero!")
	else:
		print(answer)