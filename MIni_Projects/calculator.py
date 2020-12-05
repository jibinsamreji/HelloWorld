# Calculator which does basic calculations created using functions

print("\n \n------------------------- WELCOME! ------------------------- \n")
print("CAL BUDDY IS READY TO ASSIST YOU WITH YOUR CALCULATIONS :)\n")


def ops():
    import sys
    import math

    print("\nWhat operation would you like to do now: \nPlease choose from the following\n"
          "1 --> Addition\n2 --> Subtraction\n3 --> Multiplication\n4 --> Division\n5 --> Square Root")
    print("6 --> MadLib Game\n")

    choice = input("Your choice:")

    if choice == "1":
        print("-------Addition--------\n")
        x = float(input("Enter first number:"))
        y = float(input("Enter second number:"))
        res = x + y
        print("Result: " + str(res))

    elif choice == "2":
        print("-------Subtraction--------\n")
        x = float(input("Enter first number:"))
        y = float(input("Enter second number:"))
        res = x - y
        print("Result: " + str(res))

    elif choice == "3":
        print("-------Multiplication--------\n")
        x = float(input("Enter first number:"))
        y = float(input("Enter second number:"))
        res = x * y
        print("Result: " + str(res))

    elif choice == "4":
        print("-------Division--------\n")
        x = float(input("Enter first number:"))
        y = float(input("Enter second number:"))
        res = x / y
        print("Result: " + str(res))

    elif choice == "5":
        print("-------Square Root--------\n")
        x = float(input("Enter the number:"))
        print("Result: " + str(math.sqrt(x)))

    elif choice == "6":
        print("-------Game Time - Funny Mad Libs--------\n")
        ml_game()

    else:
        print("Invalid Entry! Please try again: ")
        ops()

    cont_op = input("\nAnymore further operation? Y/N: ").capitalize()

    if cont_op == 'Y' or cont_op == 'YES':
        {
            ops()
        }
    else:
        {
            # print("\n \nThank You For Using CAL BUDDY! :)")
            sys.exit("\n \nThank You For Using CAL BUDDY! :)")

        }


def ml_game():
    fav_color = input("\n Enter your favourite color:")
    pl_noun = input("\n Enter a plural noun:")
    cel_name = input("\n Enter a celebrity name:")

    print("\n My favourite color is " + fav_color)
    print(" I have two " + fav_color + " shaded " + pl_noun)
    print(" My favourite celebrity is " + cel_name)


ops()
