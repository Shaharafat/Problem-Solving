def check_lucky_division(num, variant):
    for variant in variants:
        if num % variant == 0:
            return "YES"

    return "NO"


if __name__ == "__main__":
    num = int(input())
    variants = [4, 7, 47, 74, 44, 444, 447, 474, 477, 777, 774, 744]

    result = check_lucky_division(num, variants)
    print(result)
