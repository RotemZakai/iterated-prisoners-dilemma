#Dictionary structure is pair of strategies moves (Cooperate or Defect) and a pair of point per each combination
pointsTable = {   
    ("Cooperate", "Cooperate"): (3, 3),
    ("Cooperate", "Defect"): (0, 5),
    ("Defect", "Cooperate"): (5, 0),
    ("Defect", "Defect"): (1, 1),
}

#print(pointsTable[("Cooperate", "Cooperate")]) 

#Function that returns the points for each round depends on the move that every strategy will play
def playRound(move1, move2, game): 
    return game[(move1, move2)]

#print(playRound("Cooperate","Cooperate",pointsTable))

