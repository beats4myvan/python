submission = input()

user_points = {}
language_count = {}

while not submission == "exam finished":
    if "banned" in submission:
        username, banned = submission.split("-")
        user_points.pop(username, None)
        submission = input()
        continue
    username, language, submission = submission.split("-")
    if username not in user_points:
        user_points[username] = [int(submission)]
        if language not in language_count:
            language_count[language] = [1]
        else:
            language_count[language].append(1)
    elif username in user_points:
        user_points[username] += [int(submission)]
        language_count[language].append(1)
    submission = input()
ordered_languageCount = dict(sorted(language_count.items(), key=lambda x: (-sum(x[1]), x[0])))
ordered_points = dict(sorted(user_points.items(), key=lambda x: (-max(x[1]), x[0])))
print("Results:")
for user, points in ordered_points.items():
    print(f'{user} | {max(points)}')
print('Submissions:')
for language, counts in ordered_languageCount.items():
    print(f"{language} - {sum(counts)}")