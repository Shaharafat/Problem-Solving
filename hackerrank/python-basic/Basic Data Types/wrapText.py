import textwrap


def wrap(string, max_width):
    stringList = list(string)
    start = 0
    end = max_width
    str = ""

    while True:
        str = str + "".join(stringList[start:end]) + "\n"
        start = end
        end = end + max_width
        if start >= len(stringList):
            str = str + "\n"
            break

    return str


if __name__ == "__main__":
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
