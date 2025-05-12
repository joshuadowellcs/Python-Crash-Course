# Takes input from user using input()
seating = input("How many people are in your dinner group? ")

# Converts string into int() and does comparison 
if int(seating) > 8:
    print("You'll have to wait for a table.")
else:
    print("Your table is ready.")