'''
练习 8-9 消息
创建一个列表，其中包含一系列简短的文本消息；将这个列表传递给一个名为
show_messages() 的函数，它打印列表中的每条文本消息。
'''
def show_messages(messages):
	"""打印列表中的所有消息"""
	for message in messages:
		print(message)


messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

