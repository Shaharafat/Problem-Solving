if __name__ == "__main__":
    alphanumeric = False
    alpha = False
    digit = False
    lowercase = False
    uppercase = False

    s = input()

    for index in range(len(list(s))):
        char = s[index]
        if char.isalnum():
            alphanumeric = True
        if char.isalpha():
            alpha = True
        if char.isdigit():
            digit = True
        if char.islower():
            lowercase = True
        if char.isupper():
            uppercase = True

    print(alphanumeric)
    print(alpha)
    print(digit)
    print(lowercase)
    print(uppercase)
