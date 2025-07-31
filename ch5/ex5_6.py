age = int(input('Enter your age: '))
mes = 'The person is a'
if age < 2:
    print(mes + " baby.")
elif 2 <= age < 4:
    print(mes + ' toddler.')
elif 4 <= age < 13:
    print(mes + " kid.")
elif 13 <= age < 20:
    print(mes + ' teenager.')
elif 20 <= age < 65:
    print(mes + 'n adult.')
else:
    print(mes + 'n elder')