def breakingRecords(scores):
    least_count = 0
    max_count = 0
    max = None
    min = None

    for idx, item in enumerate(scores):
        if max == None:
            max = item
            # continue
        if min == None:
            min = item
            # continue
        print(min, max)
        if item < min:
            least_count += 1
            min = item
        if item > max:
            max_count += 1
            max = item
    return [max_count, least_count]
    print(least_count)
    print(max_count)


# breakingRecords([12, 24, 10, 24])
print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))
print(breakingRecords([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
