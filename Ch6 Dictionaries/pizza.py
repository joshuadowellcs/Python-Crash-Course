# store information about a pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# summarize the order

print(f"You ordered a {pizza['crust']}-crust pizza " "with the follwing toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")