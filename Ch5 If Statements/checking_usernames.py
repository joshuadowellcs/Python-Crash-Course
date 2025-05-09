current_users = ['Joshua', 'Mike', 'Kollie', 'Zamora', 'Donahue', 'Singleton']
new_users =['Mike', 'Soso', 'Romeo', 'Daniel', 'joshua']

# Added this line to convert current user to all caps  
# Helps with case sensitvity
current_users_upper = [user.upper() for user in current_users]

for new_user in new_users:

    # Edited this line to convert to upper to conduct comparisons
    if new_user.upper() in current_users_upper:
        print("You will need to enter a new user name!")
    else:
        print(f"{new_user} is available")

