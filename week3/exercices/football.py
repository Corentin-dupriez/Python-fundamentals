removed_players = input().split(' ')
team_a_removed_player = 0
team_b_removed_player = 0
stop_game = False

for removed_player in set(removed_players):
    if team_a_removed_player > 4 or team_b_removed_player > 4:
        stop_game = True
        break
    if removed_player[:1] == 'A':
        team_a_removed_player += 1
    elif removed_player[:1] == 'B':
        team_b_removed_player += 1

print(f'Team A - {11 - team_a_removed_player}; Team B - {11 - team_b_removed_player}')

if stop_game:
    print('Game was terminated')
