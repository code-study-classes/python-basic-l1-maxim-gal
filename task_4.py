db1 = [101, 102, 105, 108, 110]
db2 = [105, 199, 101, 115, 105]

common_users = []
for user_id in db1:
    if user_id in db2 and user_id not in common_users:
        common_users.append(user_id)

print("Совпадающие ID:", common_users)