def return_highest_sum(user: str, rating: int, highest_rating: int, highest_user: str):
    if not highest_rating or rating > highest_rating:
        return user, rating
    return highest_user, highest_rating


def highest_rankers(submissions: dict):
    sum_submissions = {}
    highest_user, highest_mark = None, 0
    for user_submission in submissions:
        sum_ratings = 0
        for x in range(len(submissions[user_submission])):
            sum_ratings += submissions[user_submission][x][1]
        sum_submissions[user_submission] = sum_ratings
    for sub, mark in sum_submissions.items():
        high_user, high_mark = return_highest_sum(sub, mark, highest_mark, highest_user)
        highest_user, highest_mark = high_user, high_mark
    print(f'Best candidate is {highest_user} with total {highest_mark} points.')


def print_contestants(submissions: dict):
    highest_rankers(submissions)
    print('Ranking:')
    for contestant in sorted(submissions):
        print(contestant)
        sorted_submissions = sorted(submissions[contestant], key=lambda x: x[1], reverse=True)
        for user_submissions in sorted_submissions:
            print(f'# {user_submissions[0]} -> {user_submissions[1]}')


contests_password = {}
all_submissions = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    contest_name, password = command.split(':')
    contests_password[contest_name] = password

while True:
    command = input()
    if command == 'end of submissions':
        break
    submission_contest, submission_password, username, points = command.split('=>')
    if contests_password.get(submission_contest) and submission_password == contests_password[submission_contest]:
        if all_submissions.get(username):
            not_found = True
            for submission in all_submissions[username]:
                if submission[0] == submission_contest:
                    if submission[1] < int(points):
                        submission[1] = int(points)
                        not_found = False
                    else:
                        not_found = False
            if not_found:
                all_submissions[username].append([submission_contest, int(points)])
        else:
            all_submissions[username] = [[submission_contest, int(points)]]


print_contestants(all_submissions)
