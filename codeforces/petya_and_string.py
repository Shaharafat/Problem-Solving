def check_string(first_string, second_string):
    for i in range(len(first_string)):
        if first_string[i] < second_string[i]:
            return -1
        elif first_string[i] > second_string[i]:
            return 1

    return 0


if __name__ == "__main__":
    first_string = str(input()).lower()
    second_string = str(input()).lower()

    result = check_string(first_string, second_string)
    print(result)
