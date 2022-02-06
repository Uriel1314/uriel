# the use of list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

# modify the element
motorcycles[0] = 'ducati'
print(motorcycles)

# append the element
motorcycles.append('ducati')
print(motorcycles)

# insert element
motorcycles.insert(0, 'uriel')
print(motorcycles)

# delete the element
del motorcycles[0]
print(motorcycles)

poped_motorcycle = motorcycles.pop()
print("pop the element is ",poped_motorcycle)
print(motorcycles)

# pop any element
last_owned = motorcycles.pop(1)
print(last_owned)
print(motorcycles)


