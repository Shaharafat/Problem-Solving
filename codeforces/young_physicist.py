# Failed
if __name__ == "__main__":
    n = int(input())
    result = 0
    for i in range(n):
        vector = list(map(lambda x: int(x), input().split(" ")))

        for j in range(3):
            result += vector[j]

    if result == 0:
        print("YES")
    else:
        print("NO")
