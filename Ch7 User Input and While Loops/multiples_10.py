# Takes an input from the user using input()
number = input("Please enter a number: ")

# Converts string number into int using int()
number = int(number)

# Compares to see if number is a multiple of 10 with % operator 
if number % 10 == 0:
    print(f"\n{number} is a multiple of 10.")
else:
    print(f"\n{number} is not a multiple of 10.")