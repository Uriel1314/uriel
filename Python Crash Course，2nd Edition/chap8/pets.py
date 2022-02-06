def describe_pet(animal_type, pet_name):
	# According to pet information
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}")

# call a function
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

# error
describe_pet('harry', 'hamster')

describe_pet(pet_name = 'harry', animal_type = 'hamster')
