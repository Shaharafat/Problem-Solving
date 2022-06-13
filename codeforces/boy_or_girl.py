def boy_or_girl(username):
    dist_char = len(list(set(username)))

    print("IGNORE HIM!" if dist_char % 2 != 0 else "CHAT WITH HER!")


if __name__ == "__main__":
    name = str(input())

    boy_or_girl(name)
