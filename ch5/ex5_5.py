alien_color = 'green'
if alien_color == 'green' :
    print("You just earn 5 point.")
elif alien_color == 'yellow':
    print("You just earn 10 points.")
else:
    print("You just earn 15 points.")

points = ['5','10','15']
message = 'You just earn '
alien_color = 'yellow'
if alien_color == 'green' :
    print(message + f"{points[0]} points.")
elif alien_color == 'yellow':
    print(message + f"{points[1]} points.")
else:
    print(message + f"{points[2]} points.")

alien_color = 'red'
if alien_color == 'green' :
    print(message + f"{points[0]} points.")
elif alien_color == 'yellow':
    print(message + f"{points[1]} points.")
else:
    print(message + f"{points[2]} points.")