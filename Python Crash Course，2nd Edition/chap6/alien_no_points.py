alien_0= {
	'color':'green',
	'speed':'slow',
}
# KeyError: 'scores'
# print(alien_0['scores'])

point_value = alien_0.get("points", 'No point value assigned.')
print(point_value)

point_value = alien_0.get("points")
print(point_value)
