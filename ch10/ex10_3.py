filename = 'texts/guest.txt'
with open(filename, 'w') as file_object:
    file_object.write("Name: " + input("Please enter yout name: ") + "\n")