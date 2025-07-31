current_users = ['Admin', 'Kyaw Kyaw', 'Bob', 'Ma Ma', 'David', 'Man Man']
current_users_lower = []
for current_user in current_users:
    current_users_lower.append(current_user.lower())
    
new_users = ['Man man', 'Kyaw Kyaw', 'Alice', 'Zoe', 'Zaw Zaw', 'Maung Maung']
new_users_lower = [] # Can use as new_users_lower = [user.lower() for user in new_users]
for new_user in new_users:
    new_users_lower.append(new_user.lower())

for user in new_users_lower:
    if user in current_users_lower:
        print(f"Username '{user.title()}' is not avaiable. You will need to enter a new username.")
    else:
        print(f"Username '{user.title()}' is available.")