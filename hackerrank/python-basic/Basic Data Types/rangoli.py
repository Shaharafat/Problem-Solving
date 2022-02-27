def print_rangoli(size):
    # Set all the characters into an array. ASCII 97 - 123
    alphabetArray = []
    for i in range(97, 123):
        alphabetArray.append(chr(i))
    # All the will start from 0 index.
    # While loop to print the number from last to first direction
    # Row and Column number will be '(size * 2) - 1'
    # Each line will contain the character of '(line_number * 2)  - 1'
    # Each line will contain '-' character (character_count * 2) // 2 on each side.
    column_count = size * 2 - 1
    column_count = column_count + column_count - 1
    counter = 1
    dash_on_each_side = 0
    dash = "-"
    actual_index_size = size
    mem_arr = []
    while size:
        character_count = counter * 2 - 1
        dash_on_each_side = (
            column_count - character_count - (character_count - 1)
        ) // 2

        # Generate centered Text
        center_string = ""
        index = size - 1
        first_index = actual_index_size - size

        for i in range(size - 1, actual_index_size):
            if i == (size - 1):
                center_string += alphabetArray[i]
            else:
                center_string = (
                    alphabetArray[i] + "-" + center_string + "-" + alphabetArray[i]
                )

        # Cache Current Value for later use
        mem_arr.append(
            f"{dash*dash_on_each_side}{center_string}{dash*dash_on_each_side}"
        )

        print(f"{dash*dash_on_each_side}{center_string}{dash*dash_on_each_side}")
        size = size - 1

        counter = counter + 1
    # Print Cached Lines
    length = len(mem_arr) - 2
    while True:
        if length < 0:
            break
        print(mem_arr[length])
        length = length - 1


print_rangoli(26)
