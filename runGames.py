import random

from payoffTable import *
from playGame import *
from strategyFunctions import *

random.seed(42)

#Play several different games - each one with different competing strategies: 

# game 1: alwaysCooperate vs. alwaysDefect -> result: (0,15)
print(playGame(alwaysCooperate, alwaysDefect, 3))

# game 2: titForTat vs. alwaysDefect -> result: (4,9)
print(playGame(titForTat, alwaysDefect, 5))

# game 3: alwaysRandom vs.titForTat -> result: (20,20) -> Note that alwaysRandom is reproducible thanks to random.seed(42) :)
print(playGame(alwaysRandom, titForTat, 7))
