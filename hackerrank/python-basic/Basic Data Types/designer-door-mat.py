if __name__ == "__main__":
    data = input()
    N, M = data.split(" ")
    N = int(N)
    M = int(M)

    # M = 3 times of N.
    # This line will run N times.
    # First line contains 1 .|. then it will increase with 2 times more.
    # On the middle line it will show WELCOME message.

    pattern = ".|."
    fill = "-"
    welcomeText = "WELCOME"
    strLine = ""
    patternCount = 1
    for i in range(0, N):
        fillCount = (M - patternCount * 3) // 2

        if i == ((N // 2)):
            fillCount = (M - 7) // 2
            strLine = fill * fillCount + welcomeText + fill * fillCount
            print(strLine)
        else:

            strLine = fill * fillCount + pattern * patternCount + fill * fillCount
            print(strLine)

        if (i + 1) >= ((N // 2) + 1):
            patternCount = patternCount - 2
        else:
            patternCount = patternCount + 2
