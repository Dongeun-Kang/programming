if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
    students.sort(key=lambda x: x[1])

    min_score = students[0][1]
    second_lowest_score = None
    for student in students:
        if student[1] > min_score:
            second_lowest_score = student[1]
            break

    result = []
    for student in students:
        if student[1] == second_lowest_score:
            result.append(student[0])

    print('\n'.join(sorted(result)))
