if __name__ == "__main__":
    number_of_problems = int(input())
    implementable_problems = 0

    for problem in range(0, number_of_problems):
        line = input()

        solution_stats = line.split(" ")  # split input line
        solvable_participants_count = 0

        for i in range(0, len(solution_stats)):
            solution_stats[i] = int(solution_stats[i])
            solvable_participants_count += solution_stats[
                i
            ]  # add all participants that solved the problem

        if solvable_participants_count >= 2:
            implementable_problems += 1

    print(implementable_problems)
