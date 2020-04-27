is_hot = False
is_cold = False

# if condition
if is_hot:
    print("It's a hot day !")
    print("Drink plenty of water")

elif is_cold:
    print("It's a cold day !")
    print("Wear warm clothes !")
else:
    print("It's a lovely day")
print("Enjoy Your Day!")


# Program to print DOWN PAYMENT
price_house = 1000000
good_credit = input("True of False : ")

if good_credit == 'True' or good_credit == 'true':
    print("Have good credit standing !")
    down_payment = price_house * 0.1
else:
    print("Have poor credit standing !")
    down_payment = price_house * 0.2
print(f"Down payment is : ${down_payment}")


# Logical Conditions using "and" "or" "not"

has_high_income = True
has_good_credit = True

if has_good_credit and has_high_income:
    print('Eligible for loan')


# Comparison Operators > < = >= <=

temp = 33

if temp > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

new_name = input("Please enter name: ")
char_count = len(new_name)

if char_count < 3:
    print("Name must be atleast 3 characters")
elif char_count > 50:
    print("Name can be a maximum of 50 characters")
else:
    print("Name looks good!")
