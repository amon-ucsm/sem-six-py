with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.lstrip() + "\n" +"*" * 50)
    
with open('../ch10/pi_digits.txt') as file_object:
    for line in file_object:
        print(line.lstrip())
    print("\n" + "*" * 50)

file_path = 'c:/Users/Asus/Desktop/vscode/pychws/ch10/pi_digits.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
    
"""for line in lines:
    print(line.strip())"""

pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string[:52] + "...")
print(len(pi_string))