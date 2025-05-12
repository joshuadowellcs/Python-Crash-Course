cities = {
    'atlanta':{
        'country': 'USA',
        'population': 10030000,
        'fact': 'peach city',
    },
    'new york city':{
        'country': 'USA',
        'population': 30000000,
        'fact': 'big apple',

    },

    'chicago': {
        'country' : 'USA',
        'population': 22000000,
        'fact': 'windy city',
        },
}

for city, facts in cities.items():
    print(f"\nThe city {city} interesting facts are:")
    for fact in facts.values():
        print(f"\t{fact}")

