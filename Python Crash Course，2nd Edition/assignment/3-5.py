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
