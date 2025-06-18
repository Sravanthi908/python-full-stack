users = [
    {"username": "alice", "followers": 100},
    {"username": "bob", "followers": 150}
]

sorted_users = []


if users[0]["followers"] > users[1]["followers"]:
    sorted_users.append(users[0])
    sorted_users.append(users[1])
else:
    sorted_users.append(users[1])
    sorted_users.append(users[0])


usernames = []


for user in sorted_users:
    usernames.append(user["username"])

print(usernames)
