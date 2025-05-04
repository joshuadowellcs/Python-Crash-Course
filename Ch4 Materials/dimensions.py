"""dimensions =(200, 50)
print(dimensions[0])
print(dimensions[1])

# This line of code will cause a type error
# dimensions[0] = 250

# Looping through all values in a tuple
for dimension in dimensions:
    print(dimension)"""

# Writing over a tuple

dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)


