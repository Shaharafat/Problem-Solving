def string_task(string_list):
    result_string = ""
    for i in range(len(string_list)):
        if string_list[i] not in ["a", "e", "i", "o", "y", "u"]:
            result_string += f".{string_list[i]}"

    return result_string


if __name__ == "__main__":
    string = str(input()).lower()
    string_list = [char for char in string]

    result_string = string_task(string_list)
    print(result_string)
