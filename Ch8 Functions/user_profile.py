def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last name'] = last
    return user_info

"""user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')

print(user_profile)"""

user_profile = build_profile('joshua', 'dowell', work_experience = 'Veteran', location = 'virginia', education = 'Computer Science')

print(user_profile)