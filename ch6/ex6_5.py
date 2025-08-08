rivers = {
    'nile': 'egypt',
    'yangtze': 'china',
    'ganges': 'india',
    'ayawaddy': 'myanmar',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("*" * 50)    
for river in rivers.keys():
    print(river.title())

print("*" * 50)
for country in rivers.values():
    print(country.title())