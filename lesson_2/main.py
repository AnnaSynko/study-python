user_1 = {
    "user_name": "tester",
    "role": "admin",
    "accont_connection": True
}

user_2 = {
    "user_name": "junior",
    "role": "user",
    "accont_connection": False
}

user_3 = {
    "user_name": "middle",
    "role": "pro_user",
    "accont_connection": True
}

list_of_users = [user_1, user_2, user_3]

for user in list_of_users:   # перебираємо кожного user в списку
    print(f"Work with user {user['user_name']} ----->>>")
    if not user["accont_connection"]:
        count_of_tries = 6
        while count_of_tries !=0: 
            if count_of_tries == 3:
                user['accont_connection'] = True
                break
            print("Try to connect to user account")
            count_of_tries -= 1
            print("Count of tries left: ", count_of_tries)
    elif user["role"] == "admin":
        print(f"Hello in system {user['user_name']}")
    else: 
        print("Welcome on the board")