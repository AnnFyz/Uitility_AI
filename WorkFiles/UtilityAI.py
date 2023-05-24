import csv

def getUtilityScore(gamestate, action):
    u = 0
    actionStateChanges = action[3:8]
    gameStateStat = gamestate[3:8]
    for a in actionStateChanges:
        weight = -math.log(gameStateStat[i])
    return u

actions = []
gamestate = ["Gamestate", "This is gameState", 999,5,5,5,5,5]
with open ("./WorkFiles\Actions.csv") as file:
    reader = csv.reader(file, delimiter= ",")
    #for row in reader:
        #print(row)

    for i, row in enumerate(reader):
        if i == 0:
            continue
        actions.append(row)

#SimulationLoop

for i in range(100):
    utilities = []
    for action in actions:
        getUtilityScore(gamestate, action)
         