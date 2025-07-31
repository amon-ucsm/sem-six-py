filename = 'texts/poll.txt'

with open(filename, 'a') as file_object:
    while True:
        response = input("Why do you like programming? (or `q` to quit): ")
        if response.lower() == 'q':
            break
        else:
            file_object.write(response + "\n")
            print("Thank you for your response!")