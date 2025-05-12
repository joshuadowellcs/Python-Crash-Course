person = {
    'first_name': 'Mike',
    'last_name': 'Williams',
    'age': 41,
    'city': 'Chesapeake',

}
"""print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])"""

person1 = {
    'first_name': 'Joshua',
    'last_name': 'Dowell',
    'age': 37,
    'city': 'Chesapeake',
}

person2 = {
    'first_name': 'Carlton',
    'last_name': 'Lundy',
    'age': 41,
    'city': 'Suffolk',
}

peoples = [person, person1, person2]

for people in peoples:
    print(f"\n{people}".title())
