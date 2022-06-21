def check_translation(word, translated_word):
    translate = word[::-1]

    return "YES" if translate == translated_word else "NO"


if __name__ == "__main__":
    word = input()
    translated_word = input()

    result = check_translation(word, translated_word)
    print(result)
