def capitalize(word):
    word = word[0:1].upper() + word[1:]
    return word


if __name__ == "__main__":
    word = str(input())

    print(capitalize(word))
