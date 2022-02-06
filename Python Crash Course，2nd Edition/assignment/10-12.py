import json 

try:
	with open('favorite_number2.json') as f:
		number = json.load(f)
except FileNotFoundError:
	number = input("What's your favorite number? ")
	with open('favorite_number2.json', 'w') as f:
		json.dump(number, f)
	print("Thanks, I'll remember that.")
else:
	print(f"I know your favorite number! It's {number}.")