import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'ch10/number.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)