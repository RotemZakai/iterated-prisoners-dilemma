from payoffTable import *
from playGame import *
from strategyFunctions import *

#Testing few edge cases to check inputs. If all is right - runs without returning Error message. If there's an Error -> returns Error message that indicates where the error is

# playRound returns the right points for one pair of moves
assert playRound("Cooperate", "Defect", pointsTable) == (0, 5)

# titForTat opens with cooperation when there is no history
assert titForTat([], 2) == "Cooperate"

# titForTat copies the opponent's last move (opponent defected)
assert titForTat([("Cooperate", "Defect")], 1) == "Defect"

# playGame sums points over rounds: cooperate vs defect, 2 rounds
assert playGame(alwaysCooperate, alwaysDefect, 2, game=pointsTable) == (0, 10)

# playGame: two cooperators get 3 points each per round
assert playGame(alwaysCooperate, alwaysCooperate, 2, game=pointsTable) == (6, 6)

# playGame: titForTat vs. alwaysDefect, 5 rounds (0+1+1+1+1 vs. 5+1+1+1+1)
assert playGame(titForTat, alwaysDefect, 5, pointsTable) == (4, 9)
