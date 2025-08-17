# Passing a list
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
usernames = ['hannah', 'ty', 'maargot']
greet_users(usernames)