# Used flag with while loop to terminate program when user types 'quit'
prompt = "\nPlease enter the toppings you would like on your pizza. "
prompt += "\nEnter 'quit' to exit the program. "


active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(f"{message.title()} will be added to the pizza!")
