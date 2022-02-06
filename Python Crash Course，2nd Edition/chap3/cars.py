cars = ['bmw','audi','toyota','subaru']
# 永久排序
cars.sort() # 从小到大
cars.sort(reverse=True) # 从大到小
print(cars)

# 临时排序
cars = ['bmw','audi','toyota','subaru']
print("Here is the original list: ")
print(cars)

print("\nHere is the sorted list: ")
print(sorted(cars))
print(sorted(cars,reverse = True))

print("\nHere is the original list again!")
print(cars)

# the length of list
print(len(cars))
cars.reverse()
print(cars)