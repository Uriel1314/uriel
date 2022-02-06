'''
练习 6-4 词汇表 2
现在你知道了如何遍历字典，请整理你为完成练习 6-3 而编写的代码，将其中的一系
列函数调用 print()替换为一个遍历字典中键和值的循环。确定该循环正确无误后，再在
词汇表中添加 5 个 Python 术语。当你再次运行这个程序时，这些新术语及其含义将自动包
含在输出中。
'''

glossary = {
'string': 'A series of characters.',
'comment': 'A note in a program that the Python interpreter ignores.',
'list': 'A collection of items in a particular order.',
'loop': 'Work through a collection of items, one at a time.',
'dictionary': "A collection of key-value pairs.",
'key': 'The first item in a key-value pair in a dictionary.',
'value': 'An item associated with a key in a dictionary.',
'conditional test': 'A comparison between two values.',
'float': 'A numerical value with a decimal component.',
'boolean expression': 'An expression that evaluates to True or False.',
}
for word, definition in glossary.items():
	print(f"\n{word.title()}: {definition}")