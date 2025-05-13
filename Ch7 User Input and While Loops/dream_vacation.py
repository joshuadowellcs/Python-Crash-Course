responses = {}

polling_active = True

while polling_active:
     # prompt for the person's name and dream vacation
     name = input("\nWhat is your name: ")
     response = input("What is your dream vacation? ")

     # store the responses in a dictionary
     responses[name] = response

     # Find out if anyone else is taking the poll
     repeat = input("Would you like to let another person respond? (yes/ no) ")
     if repeat == 'no':
          polling_active = False
    
    # Polling is complete. Show the results.
print("\n---Poll Results---")
for name, response in responses.items():
     print(f"{name} would like to visit {response}.")
