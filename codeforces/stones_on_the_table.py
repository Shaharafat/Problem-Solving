if __name__ == "__main__":
    n = int(input())
    stones = str(input())
    temp = ""
    stones_to_take = 0

    for i in range(n):
        stone = stones[i]

        if temp == stone:
            stones_to_take += 1
        temp = stone

    print(stones_to_take)
