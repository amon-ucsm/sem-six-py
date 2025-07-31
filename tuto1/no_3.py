fruits = ['Apple', 'Avocado', 'Banana', 'Watermelon', 'Grape', 'Pineapple', 'Strawberry', 'Blueberry', 'Raspberry', 'Orange', 'Mango',
          'Cherry']
print(fruits)

favorite_fruits = ['Avocado', 'Watermelon', 'Pear', 'Jackfruit', 'Guava']
for fruit in favorite_fruits:
    if fruit in fruits:
        print(f"I really like {fruit}")
