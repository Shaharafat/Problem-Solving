def steps_calculator(distance):
    if distance > 5:
        if distance % 5 == 0:
            return distance // 5
        else:
            return distance // 5 + 1
    else:
        return 1


if __name__ == "__main__":
    distance = int(input())

    steps = steps_calculator(distance)
    print(steps)
