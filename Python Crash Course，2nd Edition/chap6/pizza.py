# Pizza store information
pizza = {
	'crust': 'thick',
	'toppings':['mushrooms','extra cheese'],
}

# Overview of the pizza
print(f"You ordered a {pizza['crust']}-crust pizza "
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t"+topping)
	