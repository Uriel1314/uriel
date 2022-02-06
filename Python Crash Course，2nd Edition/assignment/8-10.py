"""
在你为完成练习 8-9 而编写的程序中，编写一个名为 send_messages() 的函数，将每
条消息都打印出来并移到一个名为 sent_messages 的列表中。调用函数 send_messages() ，
再将两个列表都打印出来，确认正确地移动了消息。
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
send_messages(messages, sent_messages)

# show Final lists
print("\nFinal lists:")
print(messages)
print(sent_messages)