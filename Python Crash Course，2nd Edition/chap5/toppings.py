requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
	print("Hold the anchovies!")

requested_toppings = ["mushrooms",'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
	print(f"Adding {requested_topping}.")

print("\nFinished making your pizza.")

requested_toppings=[]
# requested_toppings = ["mushrooms",'green peppers', 'extra cheese']
if requested_toppings:
	for requested_topping in requested_toppings:
		print(f"Adding {requested_topping}.")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

avalable_toppings = ["mushrooms",'olives','green peppers', 
						'pepperoni', 'pineapple','extra cheese']

requested_toppings = ['mushrooms','french fries', 'extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in avalable_toppings:
		print(f"Adding {requested_topping}.")
	else:
		print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza.")