if __name__ == "__main__":
    num = int(input())
    game_stat = input()
    antons_win_count = 0
    daniks_win_count = 0

    for winner in game_stat:
        if winner == "A":
            antons_win_count += 1
        else:
            daniks_win_count += 1

    if antons_win_count > daniks_win_count:
        print("Anton")
    elif antons_win_count < daniks_win_count:
        print("Danik")
    else:
        print("Friendship")
