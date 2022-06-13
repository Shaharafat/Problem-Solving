if __name__ == "__main__":
    a, b = map(lambda x: int(x), input().split(" "))
    year_count = 0

    while True:
        if a > b:
            print(year_count)
            break
        else:
            year_count += 1

        a = a * 3
        b = b * 2
