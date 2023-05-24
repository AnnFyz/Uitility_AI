
import csv
import math

def getUtilityScore(gamestate, action):
    u = 0
    actionStateChanges = action[2:8]
    gameStateStat = gamestate[2:8]
    for i, actionStat in enumerate(actionStateChanges):
        weight = -math.log(gameStateStat[i] * 0.1, 10) * 5
        u += weight * float(actionStat)
        #print(u)
    return u


def applyAction(gamestate, action):
    print(action[1])
    for i,actionStat in enumerate(action):
        if i < 3: #! 3 states
            continue
        gamestate[i] += float(actionStat)
    return gamestate

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
        utilities.append(getUtilityScore(gamestate, action))

    largestUtilityIndex =  utilities.index(max(utilities))
    bestAction = actions[largestUtilityIndex]
    gamestate = applyAction(gamestate,bestAction)
    print(f"The largest utility index: {largestUtilityIndex}")

         