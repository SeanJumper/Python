#Defining a function 
def hint_username(username):
    if len(username) < 3: 
        print("Invalid Username. Must be at least three characters long")
    else:
        print("Welcome to the team")

input_username = input("what is your username:\n")
hint_username(input_username)