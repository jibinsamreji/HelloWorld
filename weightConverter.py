weight = input("Enter Your Weight : ")
choice_flag = input("(L)bs or (K)g : ")

if choice_flag == 'K' or choice_flag == 'k':
    print(f"You are {float(weight)*2.205} pounds! ")
elif choice_flag == 'L' or choice_flag == 'l':
    print(f"You are {float(weight)*0.454} kilo grams!")
else:
    print("Wrong Choice")

