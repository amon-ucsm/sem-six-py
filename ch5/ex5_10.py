current_users = ['Joy', 'wan wan', 'miya', 'layla', 'nana']
current_user_lowers = []
for current_user in current_users:
    current_user_lowers.append(current_user.lower())

new_users = ['clint', 'zilong', 'joy', 'glue', 'NANA']
for new_user in new_users:
    if new_user.lower() in current_user_lowers:
        print(f"Username '{new_user}'  have been already used. Please enter new username!")
    else:
        print(f"Username '{new_user}' is available")