# Failed
if __name__ == "__main__":
    n = int(input())
    x = 0
    y = 0
    z = 0
    for i in range(n):
        vector = list(map(lambda x: int(x), input().split(" ")))

        x += vector[0]
        y += vector[1]
        z += vector[2]

    if x == 0 and y == 0 and z == 0:
        print("YES")
    else:
        print("NO")
