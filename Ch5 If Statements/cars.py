# Code iterates through simple list and changes bmw to all caps. 

# Start with cars list
cars = ['audi', 'bmw', 'subaru', 'toyota']

# Iterate throught list
for car in cars:

    # Checks to see if list contains bmw and converts to all caps 
    if car == 'bmw':
        print(car.upper())
    
    # Everything else will have first letter capitalized
    else:
        print(car.title())