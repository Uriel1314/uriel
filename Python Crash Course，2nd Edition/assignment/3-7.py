# 邀请一些嘉宾与你共进晚餐。
guests = ['guido van rossum', 'jack turner', 'lynn hill']

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"\nSorry, {name} can't make it to dinner.")
# Jack 无法赴约，转而邀请 Gary。
del(guests[1])
guests.insert(1, 'gary snyder')
# 重新打印邀请函。
name = guests[0].title()
print(f"\n{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
name = guests[2].title()
print(f"{name}, please come to dinner.")
# 找到了更大的餐桌，再邀请一些嘉宾。
print("\nWe got a bigger table!")
guests.insert(0, 'frida kahlo')
guests.insert(2, 'reinhold messner')
guests.append('elizabeth peratrovich')

name = guests[0].title()
print(f"{name}, please come to dinner.")

name = guests[1].title()
print(f"{name}, please come to dinner.")

name = guests[2].title()
print(f"{name}, please come to dinner.")

name = guests[3].title()
print(f"{name}, please come to dinner.")

name = guests[4].title()
print(f"{name}, please come to dinner.")

name = guests[5].title()
print(f"{name}, please come to dinner.")

# 糟糕，餐桌无法及时送达！
print("\nSorry, we can only invite two people to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

name = guests.pop()
print(f"Sorry, {name.title()} there's no room at the table.")

# 应该只剩下两位嘉宾了，向他们发出邀请。
name = guests[0].title()
print(f"{name}, please come to dinner.")
name = guests[1].title()
print(f"{name}, please come to dinner.")
# 清空名单。
del(guests[0])
del(guests[0])
# 核实名单是空的。
print(guests)
