words = {
    'tuple': "Can't be modified",
    'looping': "To iterate through each element",
    'if': "Conditional statement",
    'list': "Used to store similar data sets",
    'items()': "returns key-value pairs",
    'keys()': "prints key values when used with for loop",
    'sorted()': "sorts and then prints values when used with for loop",
    'values()': "print values assigned to keys",
    '.title()': "capitalizes first letter in word",
}

"""print(f"tuple means: {words['tuple']}")
print(f"looping means: {words['looping']}")
print(f"if means: {words['if']}")
print(f"list means: {words['list']}")"""

# Utilizing the items method to print key-value pairs with for loop

for word in words.items():
    print(word)