# Dictionary can be created using {} and defining constraints known as KEY VALUE PAIR
# Adding KEY-VALUE PAIR, Each Key should be unique
customer = {
    "name": "Jibin Reji",
    "age":  25,
    "is_verified": True

}
print(customer["name"])
# print(customer["bday"])

print(customer.get("name"))


phone_num = input("Phone Number: ")
key_dic_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "0": "Zero",

}
output = ''
for ch in phone_num:
    output += key_dic_mapping.get(ch, "!") + " "
print(output)