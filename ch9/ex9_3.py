class User():
    def __init__ (self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
    def describe_user(self):
        #print('=' * 50)
        print(f"First name: {self.f_name.title()}\nLast name: {self.l_name.title()}")
        print('=' * 25 )
    def greet_user(self):
        print("Hello " + self.l_name.title() + " " + self.f_name.title())
        print('=' * 50)
        

user1 = User('Mon Myat Oo', 'saw')
user2 = User("Minn Ko Ko", 'mg')
user3 = User("Aye Mya", 'ma')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()