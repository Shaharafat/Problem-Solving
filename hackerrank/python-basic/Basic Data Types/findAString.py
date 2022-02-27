def count_substring(str, sub_string):
    count = ab0
    for index in range(len(list(str))):
        # print(str[index])
        if str[index] == sub_string[0]:
            # print(str[index : index + len(sub_string)] == sub_string)
            if str[index : index + len(sub_string)] == sub_string:
                count += 1
                # print(str[index : index + len(sub_string)])
    # print(len(list(str)))
    return count


result = count_substring("ABCDCDC", "CDC")
print(result)
