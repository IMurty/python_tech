from prettytable import PrettyTable
import footbal as fb


teams = {}
with open('teams.txt', 'r') as f_teams:
    for team in f_teams:
        teams[team.strip()] = {
                                'games': 0,
                                'wins': 0,
                                'draws': 0,
                                'losses': 0,
                                'goals_scored': 0,
                                'goals_missed': 0,
                                'points': 0,
                                }

season = fb.generate_half_of_season(teams)
table = fb.generate_table(season, teams)

t = PrettyTable(['Место', 'Команда', 'Игры', 'Победы',	'Ничьи', 'Пораж.', 'Забит.', 'Прорущ.',	'Очки'])
pos = 1
for team in sorted(teams.keys(), key=lambda x: teams[x]['points'], reverse=True):
     t.add_row([pos, team, teams[team]['games'], teams[team]['wins'], teams[team]['draws'], teams[team]['losses'],
                teams[team]['goals_scored'], teams[team]['goals_missed'], teams[team]['points']])
     pos += 1
print(t)


if __name__ == '__main__':
    fb.print_match_result(season, 'Арсенал', 'Челси')
    fb.get_match_result(season, 'Арсенал', 'Челси')
    fb.print_match_result(season, 'ЦСКА', 'Зенит')