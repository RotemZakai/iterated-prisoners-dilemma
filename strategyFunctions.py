from os import error
import random

#Building functions for different strategies:

# 1 - Always cooperate, ignoring the history
def alwaysCooperate(history,index):
    return "Cooperate"

#print(alwaysCooperate("Defect"))

#2 - Always defect, ignoring the history
def alwaysDefect(history,index):
    return "Defect"

#print(alwaysDefect("Cooperate"))

#3 - Choose Cooperate or Defect at random 
def alwaysRandom(history,index):
    options = ["Cooperate", "Defect"]
    return random.choice(options)

#print(alwaysRandom("Cooperate"))

#4 - Tit-for-tat strategy: Cooperate on the first round, then copy the opponent's last move
def titForTat(history,index):
    if len(history) == 0: 
        return "Cooperate"
    if index == 1:
        return history[-1][1] #2nd player strategy
    elif index == 2:
        return history[-1][0] #1st player strategy
    else:
        return "ERROR"


