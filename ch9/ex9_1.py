class Restaurant():
    def __init__(self, resaturant_name, cuision_type):
        self.restaurant_name = resaturant_name
        self.cuision_type = cuision_type
    def describe_restaurant(self):
        print("+" * 50)
        print("+ Restaurant name : " + self.restaurant_name.title())
        print("+ Cuision type : " + self.cuision_type.title())
        print("+" * 50)
        print()
    def open_restaurant(self):
        print(self.restaurant_name.upper() + " is open now!")
        print()
        
restaurant1 = Restaurant("lucky", "liquier")
restaurant2 = Restaurant("one star", "BBQ")

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()