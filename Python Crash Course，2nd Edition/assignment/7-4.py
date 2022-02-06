# 练习 7-4 比萨配料
# 编写一个循环，提示用户输入一系列的比萨配料，并在用户输入'quit'时结束循环。
# 每当用户输入一种配料后，都打印一条消息，说我们会在比萨中添加这种配料。


prompt = "\nWhat topping would you like on your pizza?"
prompt += "\nEnter 'quit' when you are finished: "
while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f" I'll add {topping} to your pizza.")
    else:
        break