"""favorite_languages = {'jen': 'python', 
                      'sarah': 'c', 
                      'edward': 'rust', 
                      'phil': 'python',}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")"""

# Using for loop with dictionary to find key value pairs

"""favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")"""

# Looping through all keys in a dictionary .keys()
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = ['phil','sarah']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}.")
        
# Checks to see if name is not in dictionary
    if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll.")