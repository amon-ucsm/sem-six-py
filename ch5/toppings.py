#requested_toppings = ['mushrooms','green peppers','extra cheese']
requested_toppings =[]
if requested_toppings:
    for  requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print('Sorry, we are out of green peppers rn.')
        else:
            print('Adding ' + requested_topping + '.')
    print('\nFinished making your pizza!')
else:
    print('Are you sure want a plain pizza?')