# Returning a Dictionary
def build_person(f_name, l_name, age= ''):
    person = {'First': f_name, 'Last': l_name}
    if age:
        person['age'] = age
    return person

musician = build_person('U', 'Htoo Eain Thin', age= '45')
print(musician)