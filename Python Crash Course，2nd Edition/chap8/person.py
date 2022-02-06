def build_person(first_name, last_name, age = None):
	""" Returns a dictionary that includes a person's information """
	person={
		'first': first_name,
		'last': last_name,
	}
	if age:
		person['age'] = age
	return person

musician = build_person("jimi", 'hendrix', '20')
print(musician)


