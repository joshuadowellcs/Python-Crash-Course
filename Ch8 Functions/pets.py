# Demonstration of positional arguments
"""def describe_pet(animal_type, pet_name):
    # Display information about a pet
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
#describe_pet('harry', 'hamster') # This demonstrates what happens if you get postion wrong with arguments

# Using name, value pairs within function. Basically it will automatically know where to assign each parameter
describe_pet(animal_type='hamster',pet_name='harry')
describe_pet(pet_name, animal_type='dog')"""

def describe_pet(pet_name, animal_type= 'dog'):
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('willie')

describe_pet(pet_name='harry', animal_type='hamster')
#describe_pet() # This line will cause a type error