user_names = []
if user_names:

    for user_name in user_names:
        if user_name == 'admin':
            print(f"Hello {user_name} would you like to see a status report?")
        elif user_name:
            print(f"Hello {user_name}, thanks for logging back in.")  
else:
    print("We need to get some users.")
