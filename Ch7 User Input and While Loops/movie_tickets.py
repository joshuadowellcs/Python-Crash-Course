age = 0

while age != -1:
    age = int(input("Please enter your age or type -1 to exit program: "))
    if age == -1:
        print("Goodbye!")
    elif age < 3:
        print("Your movie ticket is free!")
        
    elif age >= 3 and age <= 12:
        print("Your ticket will cost $10!")
        
    else:
        print("Your ticket will be $15!")

