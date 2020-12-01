print(" WELCOME! \n CAL BUDDY IS READY TO ASSIST YOU WITH YOUR CALCULATIONS :)\n \n")

print(" What operation would you like to do now: \n Please choose from the following\n"
      "1 --> Addition\n2 --> Subtraction\n3 --> Multiplication\n4 --> Division\n")


def ops():
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

    else:
        print("Invalid Entry! Please try again: ")
        ops()


ops()

cont_op = input("\nAnymore further calculation? Y/N: ").capitalize()

if cont_op == 'Y' or cont_op == 'YES':
    {
        ops()
    }
else:
    {
        print("\n \nThank You For Using CAL BUDDY! :)")
    }

