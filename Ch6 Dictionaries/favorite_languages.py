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
"""favorite_languages = {
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
        print("Erin, please take our poll.")"""

# Sorting dictionary in a certain order using sorted()

"""favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll")"""

# Looping through all values in a dictionary

"""favorite_languages = {

    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

polls = ['kevin', 'aaron', 'tim', 'jen', 'sarah']

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# Looping through list of people who should take the poll
for poll in polls:
    if poll in favorite_languages.keys():
        print(f"{poll}, thanks for taking the poll!")
    else:
        print(f"{poll}, please take the poll!")"""


# Using a list within dictionary

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")

    # used another for loop since languages stores list [] values
    for language in languages:
        print(f"\t{language.title()}")