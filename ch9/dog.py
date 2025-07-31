class Dog(): # Define class named Dog that store `name` and `age`
    def __init__ (self, name, age): # Special Method
        self.name = name # Attribute
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is sitting now.")
    
    def roll_over(self):
        print(self.name.title() + " is roll over!")
        
        
my_dog =Dog('mae Lone', 6)
print(f"My dog's name is {my_dog.name.title()}.") # Accessing attribute
print(f"My dog is {str(my_dog.age)} years old.")

my_dog.sit() # Calling Method
my_dog.roll_over()

"""----------------------------------------"""
print()

your_dog=Dog('phyu Phyu', 3)
print(f"Your dog's name is {your_dog.name.title()}.") # Accessing attribute
print(f"Your dog is {str(your_dog.age)} years old.")

your_dog.sit() # Calling Method
your_dog.roll_over()