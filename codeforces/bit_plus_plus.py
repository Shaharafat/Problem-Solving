if __name__ == "__main__":
    n = int(input())
    operations = []
    x = 0
    for i in range(n):
        operation = input()
        operations.append(operation)

    for i in range(n):
        if operations[i].__contains__("++"):
            x += 1
        else:
            x -= 1

    print(x)
