favorite_places = {
    'joshua':['beach', 'apple store', 'library'],
    'soso': ['garden', 'farmers market'],
    'kids': ['park', 'movies', 'computer'],
}

# Used nested for loop so each place holder can iterate during loop
for name, places in favorite_places.items():
    print(f"{name} favorite places are: ")
    for place in places:
        print(f"\t{place}")