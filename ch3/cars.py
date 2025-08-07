cars = ['Mercedes','Audi','Lexus']
print(cars)

#Modifying value of a list at index i
cars[0] = 'Nissan'
print(cars)

#Adding elements in default method: at the end of list
cars.append('BMW')
print(cars)

#Inserting elements into a list at any index
cars.insert(0, 'GMC')
print(cars)

#Removing elements using del statement
del cars[-2]
print(cars)
print('\n')

#pop statement is unlike del, it's temp, the default pop is the last index
popped_cars = cars.pop()
print(cars)
print(popped_cars)
cars.append(popped_cars)

last_own = cars.pop(0)
print('The first car I was owned was a ' + last_own.upper() + ".")
cars.insert(0, last_own)

#remove statement can use when you don't know the index but know the elements
print(cars)
cars.remove('Nissan')
print(cars)