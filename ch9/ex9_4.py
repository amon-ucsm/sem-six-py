class Restaurant():
    def __init__(self, resaturant_name, cuision_type):
        self.restaurant_name = resaturant_name
        self.cuision_type = cuision_type
        self.number_served = 0
    def describe_restaurant(self):
        print("+" * 50)
        print("+ Restaurant name : " + self.restaurant_name.title())
        print("+ Cuision type : " + self.cuision_type.title())
        print("+" * 50)
        print()
    def open_restaurant(self):
        print(self.restaurant_name.upper() + " is open now!")
        print()
    """def restaurant(self):
        print("The number of customers the restaurant have served: " + str(self.number_served))"""
    def set_number_served(self, number):
        if number >= self.number_served:
            self.number_served = number
        else:
            print("Served number cannot be less than then!")
    def increment_number_served(self, increment):
        self.number_served += increment
        
    
restaurant = Restaurant('lucky', 'BBQ')
print(f"The number of customers the restaurant have served: {restaurant.number_served}")
restaurant.number_served = 20
print(f"The number of customers the restaurant have served: {restaurant.number_served}")
restaurant.set_number_served(50)
print(f"The number of customers the restaurant have served: {restaurant.number_served}")
restaurant.increment_number_served(50)
print(f"The number of customers the restaurant have served: {restaurant.number_served}")