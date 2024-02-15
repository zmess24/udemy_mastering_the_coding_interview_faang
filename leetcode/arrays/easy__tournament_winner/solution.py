# https://www.algoexpert.io/questions/tournament-winner

def tournamentWinner(competitions, results):
    winners = {}
    n = len(competitions)
    winner = ["", 0]
    
    for i in range(n):
        result = results[i]
        team = competitions[i][1] if result == 0 else competitions[i][0]

        if team in winners:
            winners[team] += 3
        else:
            winners[team] = 3

        if winners[team] > winner[1]:
            winner = [team, winners[team]]
    
    return winner[0]
