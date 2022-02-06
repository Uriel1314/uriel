# for value in range(1, 1_000_000):
# 	print(value)

values = list(range(1, 1_000_000))
print(sum(values))

values = [value**2 for value in range(1, 1_000_000)]
print(values)
print(max(values))
print(min(values))

