"""
练习 8-11 消息归档
修改你为完成练习 8-10 而编写的程序，在调用函数 send_messages() 时，向它传递消
息列表的副本。调用函数 send_messages() 后，将两个列表都打印出来，确认保留了原始
列表中的消息
"""

def show_messages(messages):
	"""打印列表中的所有消息。"""
	print("Showing all messages:")
	for message in messages:
		print(message)


def send_messages(messages, sent_messages):
	"""打印每条消息，再将其移到列表 sent_messages 中。"""
	print("\nSending all messages:")
	while messages:
		current_message = messages.pop()
		print(current_message)
		sent_messages.append(current_message)


messages = ["hello there", "how are u?", ":)"]
show_messages(messages)

sent_messages = []
# Here a copy of the transfer is sent_messages
send_messages(messages[:], sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)