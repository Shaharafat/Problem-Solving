def decide(word):
    hello = {0: "h", 1: "e", 2: "l", 3: "l", 4: "o"}

    char_matched = 0

    for item in hello.values():
        for idx, char in enumerate(word):
            if item == char:
                word = word[idx + 1 : len(word)]
                char_matched += 1
                break

    return "YES" if char_matched == 5 else "NO"


if __name__ == "__main__":
    word = input()

    result = decide(word)
    print(result)
