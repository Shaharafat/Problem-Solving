import math

if __name__ == "__main__":
    inputs = input()

    [n, m, a] = inputs.split(" ")
    n = int(n)
    m = int(m)
    a = int(a)

    stone_count = 0

    i = math.floor(n / a)
    j = math.floor(m / a)

    if n % a != 0:
        i += 1
    if m % a != 0:
        j += 1
    stone_count = i * j

    print(int(stone_count))
