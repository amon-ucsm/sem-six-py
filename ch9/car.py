class Car(): # Class definition for a car
    """A simple attempt to model a car."""
    def __init__ (self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # Sets default calue for an attrubute
        
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.upper()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.") 
        
    def update_odometer(self, mileage): # Method for updating atribute value through a method
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles): #Incrementing an Attribute’s Value Through a Method
        self.odometer_reading += miles
    
my_new_car = Car('bmw', 'm5', 2020)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 23 # Directly modifying the attribute
my_new_car.read_odometer() # Reading the updated odometer value

my_new_car.update_odometer(30)
my_new_car.read_odometer()

my_used_car = Car('toyota', 'civic', 2018)
print(my_used_car.get_descriptive_name().title())
my_used_car.update_odometer(23000)
my_used_car.read_odometer()
my_used_car.increment_odometer(500)
my_used_car.read_odometer()