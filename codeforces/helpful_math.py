def helpful_math(string):
    numbers = sorted(string.split("+"))
    return "+".join(numbers)


if __name__ == "__main__":
    summans = str(input())

    print(helpful_math(summans))
