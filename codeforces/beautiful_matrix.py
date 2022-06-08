if __name__ == "__main__":
    matrix = []
    row_idx = 0
    col_idx = 0
    steps = 0
    for i in range(5):
        data = input()
        matrix.append(data.split(" "))
        if matrix[i].__contains__("1"):
            row_idx = i
            col_idx = matrix[i].index("1")

    if row_idx > 2:
        steps += row_idx - 2
    elif row_idx < 2:
        steps += 2 - row_idx

    if col_idx > 2:
        steps += col_idx - 2
    elif col_idx < 2:
        steps += 2 - col_idx

    print(steps)
