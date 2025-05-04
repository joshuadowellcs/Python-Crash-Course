pizzas = ['pepperoni','vegetable', 'pineapple']

friend_pizzas = pizzas[:]

friend_pizzas.append('sausage')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)