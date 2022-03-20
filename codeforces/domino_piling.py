import math

if __name__ == "__main__":
    data = input()
    max_dominoes = 0
    [M, N] = data.split(" ")
    M = int(M)
    N = int(N)

    if (M * N) % 2 == 0:
        print(int((M * N) / 2))
        max_dominoes = int((M * N) / 2)
    else:

      m = math.floor(M / 2)
      n = math.floor(N / 2) if N >= 2 else 1

      max_dominoes = m * n


