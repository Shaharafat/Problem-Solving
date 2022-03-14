if __name__ == "__main__":
    weight = int(input())

    result = weight % 2 == 0
    
    if weight == 0 or weight == 2:
        print("NO")
    elif result == True:
        print("YES")
    elif result == False:
        print("NO")
