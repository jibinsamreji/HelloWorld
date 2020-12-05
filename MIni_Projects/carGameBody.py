print("Welcome player! Type 'help' for more options..!")
user_input = input(">")
i = 0
start = False
stop = False
while user_input.upper() == "HELP":
    if i < 1:
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit""")
    i += 1
    game_option = input(">").upper()
    if game_option == 'START':
        if not start:
            print("Car started....Ready to go!")
            start = True
            stop = False
        else:
            print("Car already started....!")
    elif game_option == 'STOP':
        if not stop:
            print("Car stopping...Car stopped!")
            stop = True
            start = False
        else:
            print("Car already stopped....!")

    elif game_option == 'QUIT':
        print("Quitting.....")
        break
    else:
        print("Not a valid choice..! Please select an option from the above!")
else:
    print("I don't understand that..")







