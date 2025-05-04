# Excercise 4-10 to practice slicing

cars = ['corvette', 'mustang','supra', 'challenger', 'camry', 'mercedes', 'bmw']

print("The first three items on the list are:")

for car in cars[:3]:
    print("\n",car)

print("\nThree item from the middle of the list are:")
for car in cars[2:5]:
    print("\n",car)

print("\nThe last three items in the list are:")
for car in cars[-3:]:
    print("\n",car)
