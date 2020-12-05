names = ['Emily', 'Reji', 'Jeffin', 'Jibin']
print(names)
print(names[0])
print(names[1])
print(names[-1])
print(names[-2])

print(names[0:2])  # accessing using index values
print(names[:1])
print(names[2:])

# Finding the Largest and Smallest number in a List
num_list = [1, 2, 4, 1, 8, -1, 3]
highest_val = num_list[0]
smallest_val = num_list[0]
for each_value in num_list:
    if each_value > highest_val:
        highest_val = each_value
    elif each_value < smallest_val:
        smallest_val = each_value


print(f'Highest number in the list is: {highest_val}')
print(f'Lowest number in the list is: {smallest_val}')

# 2-Dimensional List in Python

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)

# List Operations
numbers = [5, 2, 1, 5, 7, 5, 4, 2]
# only adds at the end of the list
print(numbers)
numbers.insert(0, 3)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
# deletes the last
print(numbers)

# checking existence of an item
print((numbers.index(1)))
print(50 in numbers)

# copying a list
numbers2 = numbers.copy()

# count of item
print(numbers.count(5))
# sort- ascend & desc
numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

numbers.clear()
print(numbers)

# Program to remove duplicates in a ist
list_new = [2, 3, 1, 2, 3, 4]
output_list = []
print(list_new)
for list_numbers in list_new:
    if list_numbers not in output_list:
        output_list.append(list_numbers)
output_list.sort()
print(output_list)
