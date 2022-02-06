my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are: ")
print(friend_foods)

print(my_foods == friend_foods)
print(my_foods is friend_foods)
print(id(friend_foods))
print(id(my_foods))

# 这行不通
other_foods = my_foods
print(other_foods)
print(other_foods is my_foods)
print(id(other_foods), id(my_foods))

other_foods.append('ice cream')
print(other_foods, my_foods)
