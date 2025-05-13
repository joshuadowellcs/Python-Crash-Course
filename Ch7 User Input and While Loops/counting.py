# Avoiding infinite loops
x = 1
while x <= 5:
    print(x)
    x += 1  # if removing this line of code it will cause an infinite loop
    