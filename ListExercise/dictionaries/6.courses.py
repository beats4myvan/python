register = input()

courses = {}
while not register == "end":
    register = register.split(" : ")
    courseName = register[0]
    studentName = register[1]
    if courseName not in courses:
        courses[courseName] = [studentName]
    elif courseName in courses:
        courses[courseName].append(studentName)
    register = input()

course = sorted(courses.items(), key=lambda x: len(x[1]), reverse=True)
for key, value in course:
    print(f'{key}: {len(value)}')
    asc_value = sorted(value)
    for i in asc_value:
        print(f'-- {i}')

