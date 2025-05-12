numbers = {'Dad': [31, 24, 55],
           'Mom': [26, 5, 9],
           'Daniel': [7, 7, 7],
           'Joshua': [22, 27, 52],
           }

"""print(numbers['Dad'])
print(numbers['Mom'])
print(numbers['Daniel'])
print(numbers['Joshua'])"""

for name, favorite_numbers in numbers.items():
    print(f"\n{name} favorite numbers are:")
    for favorite_number in favorite_numbers:
        print(f"\t{favorite_number}")