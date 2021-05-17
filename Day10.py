#Inputs & Limited Error Handling

User_input_name = input("What is your name? \n")
if not User_input_name.isalpha(): 
    print("Invalid Input")
else: 
    print(User_input_name)

User_input_age = input("What age are you? \n")
if not User_input_age.isdigit():
    print("Invalid Input")
else: 
    print(int(User_input_age))

#
#print(int(User_input_age))

    

#print(int(User_input_age))