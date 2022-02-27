# Complete the solve function below.
def solve(s):
    # Split sentence into words
    str_array = s.split(" ")
    converted_arr = []
    # for i in range(len(str_array)):
    #     # Check the character is lowercase or not.
    #     if ord(str_array[i][0]) >= 97:
    #         # if lowercase, make word a list
    #         str_list = list(str_array[i])
    #         # Store first character
    #         first_char = str_list[0]
    #         # Remove first character
    #         str_list.remove(str_list[0])
    #         # Insert converted character into the first index
    #         str_list.insert(0, chr(ord(first_char) - 32))
    #         # Add it to converted_arr list
    #         converted_arr.append(("").join(str_list))
    #     else:
    #         # if uppercase, add it to converted_arr list as it is.
    #         converted_arr.append(str_array[i])
    # print((" ").join(converted_arr))
    # return (" ").join(converted_arr)
    converted_arr = []
    for i in range(len(str_array)):
        str_list = list(str_array[i])
        for j in range(len(str_list)):
            if j == 0 and ord(str_list[j]) >= 97 and ord(str_list[j]) <= 122:
                char = str_list[j]
                str_list.remove(str_list[j])
                str_list.insert(j, chr(ord(char) - 32))
            elif j != 0 and ord(str_list[j]) >= 65 and ord(str_list[j]) <= 96:
                char = str_list[j]
                str_list.remove(str_list[j])
                str_list.insert(j, chr(ord(char) + 32))

        converted_arr.append(("").join(str_list))
    # print(converted_arr)
    print((" ").join(converted_arr))
    return (" ").join(converted_arr)


# First split into words
# Split word into characters
# If index 0 is lowercase convert it to upper
# other characters will be checked and converted to lowercase if uppercased
# make the word join

#  do it until all words

# join all words with spaces


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = solve(s)

    # fptr.write(result + "\n")

    # fptr.close()
