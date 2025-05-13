# Moving items from one list to another
sandwich_orders = ['turkey', 'pastrami', 'ham', 'veggie', 'pastrami', 'philly cheese', 'tuna', 'BLT', 'pastrami']

finished_sandwiches = []

print("The deli has run out of pastrami")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sandwich_orders:
    print(f"\nI made your {sandwich} sandwich.")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    finished_sandwiches.append(current_sandwich)

for finished_sandwich in finished_sandwiches:
    print(f"\nThese sandwiches were made {finished_sandwich}")