# Introducing while loops
"""current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1 # Same thing as current_number = current_number + 1"""

# using continue in a loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)