alien_0 = {'color':'green', "points":5}
print(alien_0['color'])
print(alien_0['points'])

for alien in alien_0:
	print(alien)


print()

new_points = alien_0['points']
print(f"You just earned {new_points} points")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


alien_0={'color':'green'}
print(f"The alien is {alien_0['color']}")

alien_0={'color':'yellow'}
print(f"The alien is {alien_0['color']}")

alien_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
print(f"Original x_position: {alien_0['x_position']}")

# 向右边移动外星人
# 根据当前速度确定外星人向右移动多远。
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

# 在原来的基础上加上移动距离
alien_0['x_position'] += x_increment

print(f"New x_position: {alien_0['x_position']}.")

for alien in alien_0:
	print(alien)

# Delete key/value pair
alien_0 = {'color':'green', 'points':5}
del alien_0['points']
print(alien_0)

