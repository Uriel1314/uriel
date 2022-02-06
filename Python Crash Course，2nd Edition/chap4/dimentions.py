dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# modify the element
# TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 250 

my_t = (3,)
print(id(my_t), type(my_t))
my_s = (3)
print(id(my_s), type(my_s))

# modify the tuple
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified the dimensions:")
for dimension in dimensions:
	print(dimension)
