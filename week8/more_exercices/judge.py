def print_participants(all_submissions: dict, type_submission: str):
    participants_for_topic = []
    for participant, submission in all_submissions.items():
        for topic, rating in submission[0].items():
            if topic == type_submission:
                participants_for_topic.append([participant, rating])
    print(f'{type_submission}: {len(participants_for_topic)} participants')
    for participant_in_topic in participants_for_topic:
        print(f'{participant_in_topic[0]} <:> {participant_in_topic[1]}')


participants_submissions = {}
participants_ratings = {}
all_topics = []

while True:
    command = input()
    if command == 'no more time':
        break
    username, contest, points = command.split(' -> ')
    if not participants_submissions.get(username):
        participants_submissions[username] = [{contest: int(points)}]
        participants_ratings[username] = int(points)
    elif participants_submissions.get(username) and not participants_submissions[username][0].get(contest):
        participants_submissions[username].append({contest: int(points)})
        participants_ratings[username] += int(points)
    elif participants_submissions.get(username) and participants_submissions[username][0].get(contest):
        participants_ratings[username] += (int(points) - participants_submissions[username][0][contest])
        participants_submissions[username][0][contest] = int(points)
    if contest not in all_topics:
        all_topics.append(contest)

print(participants_submissions)
print(participants_ratings)

for topic in all_topics:
    print_participants(participants_submissions, topic)