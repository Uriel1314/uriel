'''
# 首先创建一个列表，其中包括一些要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止。
# 打印每个设计后，都将其迁移到列表completed_models里
while unprinted_designs:
	current_design = unprinted_designs.pop()
	print(f"Printing model: {current_design}")
	completed_models.append(current_design)

# demonstrates all the printed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)
'''

# Improved version
def print_model(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print(f"Printing model: {current_design}")
		completed_models.append(current_design)

def show_completed_models(completed_models):
	# demonstrates all the printed models
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)


# 首先创建一个列表，其中包括一些要打印的设计
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# call functions
print_model(unprinted_designs, completed_models)
show_completed_models(completed_models)