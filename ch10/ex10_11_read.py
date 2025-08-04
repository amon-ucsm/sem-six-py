import json

filename = 'ch10/ex10_11.json'

try:
    with open(filename) as f_obj:
        fav_num = json.load(f_obj)
except FileNotFoundError:
    print("We cannot find the file")
else:
    print("I know your favorite number! It's " + fav_num + ".")