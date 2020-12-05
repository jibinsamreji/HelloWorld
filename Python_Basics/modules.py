# modules help to reuse as
# well as organize our codes


def lbs_to_kg(weight):
    return weight * 0.45


def kg_to_lbs(weight):
    return weight / 0.45


def find_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    print(f"Max number is {max_num}")
