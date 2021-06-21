# # in the database
# username = 'yuliia'
# password = 'password'
#
# admin_username = 'admin'
# admin_password = 'admin'
#
# user_is_auth = False
#
# while not user_is_auth:
#     username_input = input("Enter your username: ")
#     password_input = input("Enter your password: ")
#
#     if username_input == username and password_input == password:
#         print("Success auth")
#         user_is_auth = True
#     elif username_input == admin_username and password_input == admin_password:
#         print("Success auth. Hello dear admin!")
#         user_is_auth = True
#     elif username_input == 'hack' or password_input == 'hack':
#         print("Success auth. Hello dear hacker!")
#         user_is_auth = True
#     else:
#         if username_input != username:
#             print("Username is incorrect")
#         if password_input != password:
#             print("Password is incorrect")
#         print("Try again...\n")
# print("Congratulations !!!!")
#
# var = 0
#
# while var < 10:
#     print("Test while loop")
#     var += 1
#
# for var in range(10):
#     print("Test for")
#
# print("Done")

# Functions
def greeting(name):
    print('Hello', name)

greeting('Yuliia')
greeting('Dima')

def parabola(x):
    print(x**2)

parabola(2)
parabola(-2)

from pprint import pprint

players = [
    {
        "name": "John Doe",
        "heigh": 2.1
    },
    {
        "name": "Peter Parker",
        "heigh": 1.9
    },
    {
        "name": "Tonny Stark",
        "heigh": 2.0
    },
]


def add_player(name, heigh):
    players.append({
        "name": name,
        "heigh": heigh
    })


def remove_player(name):
    index = 0
    for player in players:
        if player["name"] == name:
            del players[index]
        else:
            index += 1


add_player("New player", 2.2)
add_player("New player 2", 3.2)
add_player("New player 3", 2.3)

remove_player("Peter Parker")
remove_player("New player 2")

pprint(players)
