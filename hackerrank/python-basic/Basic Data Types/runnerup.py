if __name__ == "__main__":

    n = int(input())
    arr = map(int, input().split())

    arr = list(arr)
    sortedList = arr.sort(reverse=True)
    champion = arr[0]
    for item in arr:
        if item != champion:
            runnersup = item
            print(runnersup)
            break
