def is_nearly_lucky_number(number):
    count_lucky_numbers = 0
    for digit in number:
        if int(digit) == 4 or int(digit) == 7:
            count_lucky_numbers += 1

    if count_lucky_numbers == 4 or count_lucky_numbers == 7:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    number = input()

    result = is_nearly_lucky_number(number)

    print(result)
