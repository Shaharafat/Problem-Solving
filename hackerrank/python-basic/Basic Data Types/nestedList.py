if __name__ == "__main__":
    scores = []
    studentsScoreRecords = []
    secondlowest = 0
    students = []
    for _ in range(int(input())):
        record = []
        name = input()
        score = float(input())
        scores.append(score)
        record.append(name)
        record.append(score)

        studentsScoreRecords.append(record)

    scores.sort()
    for score in scores:
        if score > scores[0]:
            secondlowest = score
            break

    for name, score in studentsScoreRecords:
        if score == secondlowest:
            students.append(name)

    students.sort()
    for name in students:
        print(name)

    # print(secondlowest)
