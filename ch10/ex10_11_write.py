import json

filename = 'ch10/ex10_11.json'
fav_nums = input("Enter your favorite number: ")
with open(filename, 'w') as f_obj:
     json.dump(fav_nums, f_obj)
