def city_country(city_name1, country_name1):
    cityCountry = f"{city_name1}, {country_name1}"
    return(cityCountry.title())

cities = city_country('atlanta', 'united states')
print(cities)

cities = city_country('chicago', 'united states')
print(cities)

cities = city_country('new york', 'united states')
print(cities)

