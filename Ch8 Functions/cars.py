def build_cars(manufacturer, model_name, **car_info):
    car_info['car_maker'] = manufacturer
    car_info['car_model'] = model_name
    return car_info

car_profile = build_cars(
    'ford', 'mustang',
    location = 'Virginia',
    color = 'blue'
)

print(car_profile)

