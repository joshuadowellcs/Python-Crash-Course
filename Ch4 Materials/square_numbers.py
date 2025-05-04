# Start with an empty list called squares
squares = []

# Create a loop that iterates through the range 1-10 
for value in range(1,11):

    # The current value is squared and assigned to the variable square
    square = value ** 2

    # Each new square is appended(added) to the squares list
    squares.append(square)

print(squares)



# Concise version of the above code
squares = []
for value in range(1,11):
    squares.append(value**2)
print(squares)