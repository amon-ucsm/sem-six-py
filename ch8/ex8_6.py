def city_country(city, country):
    formatted = '"' + city.title() + ", " + country.title() + '"' 
    return formatted
chile = city_country('santiage', 'chile')
myanmr = city_country('mandalay', 'myanmar')
japan = city_country('tokyo', 'japan')

print(chile)
print(myanmr)
print(japan)