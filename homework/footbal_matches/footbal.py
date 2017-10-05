import random


def generate_match():
    game_score = (random.randint(0, 20), random.randint(0, 20))
    return game_score

def generate_half_of_season(teams):
    season = {}
    teams_count = len(teams)
    list_of_teams = list(teams.keys());
    # print(list_of_teams)
    for i in range(len(list_of_teams)):
        for j in range(i + 1, len(list_of_teams)):
            team1 = list_of_teams[i]
            team2 = list_of_teams[j]
            season.update({(team1, team2): generate_match()})
    return season

def generate_table(season, teams):
    it = 0
    for match in season:
        it += 1
        # print(match)
        # print(season[match])
        team1 = match[0]
        team2 = match[1]
        team1_score = season[match][0]
        team2_score = season[match][1]
        # print(teams[team1])
        # print(teams[team2])
        if team1_score > team2_score:
            teams[team1]['wins'] += 1
            teams[team1]['points'] += 3

            teams[team2]['losses'] += 1
        elif team1_score < team2_score:
            teams[team1]['losses'] += 1
            teams[team2]['wins'] += 1
            teams[team2]['points'] += 3
        else:
            teams[team1]['draws'] += 1
            teams[team2]['points'] += 1

            teams[team2]['draws'] += 1
            teams[team2]['points'] += 3

        teams[team1]['games'] += 1
        teams[team2]['games'] += 1

        teams[team1]['goals_scored'] += team1_score
        teams[team2]['goals_scored'] += team2_score

        teams[team1]['goals_missed'] += team2_score
        teams[team2]['goals_missed'] += team1_score


def print_match_result(season,team1, team2):
    if (team1, team2) in season:
        res = season[(team1, team2)]
        print(team1, res[0], '-', res[1], team2)
    else:
        print("This match does not exist")


def get_match_result(season, team1, team2):
    if (team1, team2) in season:
        return season[(team1, team2)]
    else:
        return 0