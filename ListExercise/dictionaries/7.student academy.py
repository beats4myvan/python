n_rows = int(input())

studentGrades = {}
fin_grade = {}
for _ in range(n_rows):
    name = input()
    grade = float(input())
    if name not in studentGrades:
        studentGrades[name] = [grade]
    else:
        studentGrades[name] += [grade]
for name, grade in studentGrades.items():
    averageGrade = sum(grade) / len(grade)
    if averageGrade >= 4.5:
        fin_grade[name] = averageGrade

fin_grade = sorted(fin_grade.items(), key=lambda x: x[1], reverse=True)

for name, grade in fin_grade:
    print(f'{name} -> {grade:.2f}')
