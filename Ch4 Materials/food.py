# Copying a list example

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]

my_foods.append('cannoli')
friends_food.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friends favorite foods are:")
for food in friends_food:
    print(food)

# Example of copying a list without a slice and why it does not work. Both variables point to the same list

"""my_foods = ['pizza', 'falafel', 'carrot cake']

friends_food = my_foods

my_foods.append('canoli')
friends_food.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friends_food)"""


