def pageCount(n, p):
    num_of_max_turn = n // 2

    turns_from_front = p // 2
    turns_from_rear = num_of_max_turn - turns_from_front

    return turns_from_front if turns_from_front < turns_from_rear else turns_from_rear


print(pageCount(6, 2))
print(pageCount(5, 4))
