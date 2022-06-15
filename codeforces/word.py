def manipulate_word(word):
    capital = 0
    small = 0

    for char in word:
        if char.isupper():
            capital += 1
        else:
            small += 1

    if capital > small:
        return word.upper()
    else:
        return word.lower()


if __name__ == "__main__":
    word = str(input())

    result = manipulate_word(word)
    print(result)
