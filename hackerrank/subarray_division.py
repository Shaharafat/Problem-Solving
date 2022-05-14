def birthday(s, d, m):
    segments_list = s
    count = 0

    for idx in range(0, len(segments_list) - m + 1):
        value = 0
        for i in range(idx, idx + m):
            value += segments_list[i]

        if value == d:
            count += 1
    print(count)
    return count


birthday([1, 2, 1, 3, 2], 3, 2)
birthday([1, 1, 1, 1, 1, 1], 3, 2)
birthday([4], 4, 1)
