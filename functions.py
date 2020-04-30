# def-defining a function, leave two spaces down after definition
# return-used to return data from a defined function


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


# Parameters in functions defined inside ()
print("Start")
greet_user("Jibin", "Reji")
greet_user("Emily", "Reji")

greet_user(last_name="Reji", first_name="Jeffin")

print("Finish")


def square(number):
    return number * number


print(square(3))
