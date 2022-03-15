def calculate(first_line_input, second_line_input):

    [n, k] = first_line_input.split(" ")
    scores = second_line_input.split(" ")

    n = int(n)
    k = int(k)
    next_round_participants_count = 0

    # Convert all items to integer
    scores = [int(x) for x in scores]

    place_value = int(scores[k - 1])

    for i in range(0, len(scores)):
        if scores[i] > place_value and scores[i] > 0:
            next_round_participants_count += 1
        elif scores[i] == place_value and place_value != 0:
            next_round_participants_count += 1

    return next_round_participants_count


if __name__ == "__main__":
    first_line_input = input()
    second_line_input = input()

    result = calculate(first_line_input, second_line_input)
    print(result)
