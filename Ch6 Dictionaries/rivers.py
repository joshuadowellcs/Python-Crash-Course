rivers = {
    'nile': 'egypt',
    'amazon river': 'brazil',
    'yangtze': 'china',
}
# To print a statement about each river I had to use a for loop and set conditions of when
# print a certain sentence. compare loop value to rivers['..'] and if true print statement
for river in rivers.values():
    if river == rivers['nile']:
        print(f"The nile runs through {river}")
    elif river == rivers['amazon river']:
        print(f"\nThe amazon river runs through {river}")
    else:
        print(f"\nThe yangtze runs through {river}")

# Using a loop to print the name of each river included in the dictionary
"""for river in rivers.keys():
    print(river)"""

# Using a for loop to print the name of each country
"""for river in rivers.values():
    print(river)"""
    
    