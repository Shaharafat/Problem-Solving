if __name__ == "__main__":
    data = input()
    max_dominoes = 0
    [M, N] = data.split(" ")
    M = int(M)
    N = int(N)
    m = n = remaining_m = remaining_n = 0

    total_domino = 0

    if M % 2 != 0:
        m = M - 1
        remaining_m = M % 2
    else:
        m = M

    if N % 2 != 0:
        n = N - 1
        remaining_n = N % 2
    else:
        n = N

    # set from even pair
    total_domino = (m * n) // 2

    if remaining_m:
        total_domino += N // 2
    if remaining_n:
        total_domino += M // 2

    print(total_domino)
