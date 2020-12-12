command = input()

companies = {}
while not command == "End":
    company, employee = command.split(" -> ")
    if company not in companies:
        companies[company] = [employee]
    elif employee in companies[company]:
        command=input()
        continue

    else:
        companies[company] += [employee]
    command = input()

companies = dict(sorted(companies.items(), key=lambda x: x))
for companyName, employeeId in companies.items():
    print(companyName)
    for i in employeeId:
        print(f"-- {i}")
