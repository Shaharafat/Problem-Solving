def determine_situation(sequence):
    same_sequence = sequence[0]
    count = 1

    for i in range(1, len(sequence)):
        if sequence[i] == same_sequence:
            count += 1
            if count >= 7:
                return "YES"
        else:
            count = 1
            same_sequence = sequence[i]

    return "NO"


if __name__ == "__main__":
    sequence = str(input())

    result = determine_situation(sequence)
    print(result)
