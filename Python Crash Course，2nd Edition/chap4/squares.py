squares = []
print(squares)

for vaule in range(1,11):
	square = vaule**2
	squares.append(square)

print(squares)

print(min(squares)) # min
print(max(squares))	# max
print(sum(squares)) # sum

squares = [vaule**3 for vaule in range(1,11)]
print(squares)
