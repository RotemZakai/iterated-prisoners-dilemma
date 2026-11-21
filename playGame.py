from payoffTable import *
from strategyFunctions import *

"""Play several rounds between two strategies and return their total scores.
    strategy1, strategy2: strategy functions, each called as strategy(history, index)
    rounds: number of rounds to play
    game: payoff table mapping a pair of moves to a pair of points
    Returns (strategy1Points, strategy2Points)"""

def playGame(strategy1, strategy2, rounds, game = pointsTable):
    history = []
    strategy1Points = 0
    strategy2Points = 0
    
    for i in range(rounds):
        move1 = strategy1(history,1)
        move2 =  strategy2(history,2)
        points = playRound(move1, move2, game)
        strategy1Points = strategy1Points + points[0]
        strategy2Points = strategy2Points + points[1]
        history.append((move1, move2))
    return strategy1Points, strategy2Points

#print(playGame(alwaysCooperate, titForTat, 5))
#print(playGame(titForTat, alwaysDefect, 5))
#print(playGame(alwaysDefect, titForTat, 5))