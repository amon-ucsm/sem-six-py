filename = 'texts/guest_book.txt'

with open(filename, 'w') as fiel_object:
    while True:
        name = input("Please enter yout name (or `q` to quit): ")
        if name.lower() == 'q':
            break
        else:
            print(f"Hello, {name}!")
            fiel_object.write("Nmae: " + name + "\n")