def product(A, B):

    for i in range(len(A)):
        for j in range(len(B)):
            print((int(A[i]), int(B[j])), end=" ")


if __name__ == "__main__":
    A = input()
    B = input()
    A = A.split(" ")
    B = B.split(" ")
    product(A, B)
