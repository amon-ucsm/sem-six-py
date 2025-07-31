names = []
print("Enter names (press Enter to finish):")
while True:
    name  = input().strip()
    if name == "":
        break
    names.append(name)

number_of_peoles = len(names)
if number_of_peoles == 0:
    print("The room is empty.")
elif number_of_peoles == 1 or number_of_peoles == 2:
    print("The room not being crowded.")
elif 3 <= number_of_peoles <= 5: # number_of_people >=3 and number_of_people <=5
    print("The room being crowded.")
else:
    print("There being a mob in the room.")
