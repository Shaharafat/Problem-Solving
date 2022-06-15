def substract(number, times):
    for i in range(times):
        if number % 10 == 0:
            number = number // 10
        else:
            number -= 1

    return number


if __name__ == "__main__":
    number, times = map(lambda x: int(x), str(input()).split(" "))

    result = substract(number, times)
    print(result)
