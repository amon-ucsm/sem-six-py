cities = {
    "Naypyitaw": {
        "country": "Myanmar",
        "population": "1.7 million",
        "fact": "Naypyitaw is know as city of Kingdom",
    },
    "Tokyo": {
        "country": "japan",
        "population": "37.4 million",
        "fact": "Tokyo is the most populous city in the world known it as the city of lights",
    },
    "Shanghin": {
        "country": "China",
        "population": "24.2 million",
        "fact": "Shanghai is the largest city in China and known as the city of dreams",
    },
}

print("Cities Information")
print("=" * 30)
for city_name, city_info in cities.items():
    print(f"City: {city_name}")
    print(f"Country: {city_info['country']}")
    print(f"Population: {city_info['population']}")
    print(f"Fact: {city_info['fact']}")
    print("-" * 50)

print("\n" + "=" * 50)
print("Complete dictionary of cities")
print("=" * 50)
for city_name, city_info in cities.items():
    print(f"{city_name}: {city_info}")