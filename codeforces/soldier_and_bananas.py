def calculate(k, n, w):
    total_cost = 0
    for i in range(w):
        total_cost += k * (i + 1)

    if total_cost > n:
        return total_cost - n
    else:
        return 0


if __name__ == "__main__":
    k, n, w = [int(num) for num in input().split(" ")]

    result = calculate(k, n, w)
    print(result)
