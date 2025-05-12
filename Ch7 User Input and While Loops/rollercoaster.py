# Use the int() to convert string to int value
height = input("How tall are you, in inches? ")
height = int(height)

if height > 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")