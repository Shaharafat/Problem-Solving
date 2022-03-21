if __name__ == "__main__":
    lines = int(input())

    for i in range(0, lines):
        word = input()

        if len(word) > 10:
            print(f"{word[0]}{len(word)-2}{word[-1]}")
        else:
            print(word)
