def determine_seats(stops_stats):
    max_pessenger = 0
    total_passenger = 0
    for i in range(len(stops_stats)):
        a, b = stops_stats[i]

        total_passenger -= a
        total_passenger += b
        if total_passenger > max_pessenger:
            max_pessenger = total_passenger

    return max_pessenger


if __name__ == "__main__":
    n = int(input())
    stats = []
    for i in range(n):
        stats.append(list(map(lambda x: int(x), str(input()).split(" "))))

    result = determine_seats(stats)
    print(result)
