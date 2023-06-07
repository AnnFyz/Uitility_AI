
import csv
import math

def get_utility_score(gamestate, action):
    u = 0
    action_stats_ = action[3:]
    gamestate_stats = gamestate[3:]
    for i, action_stat in enumerate(action_stats_):
        if action_stats_[i] == 0:
            continue

        weight = -math.log(max(gamestate_stats[i], 0.01) * 0.1, 10) * 5
        u += weight * float(action_stat)
        #print(u)
    return u


def apply_action(gamestate, action):
    print(action[1])
    for i,action_stat in enumerate(action):
        if i < 3: #! 3 states (name, describtion and cooldown we skip)
            continue
        gamestate[i] += int(action_stat)
    return gamestate


def load_actions():
    actions = []
    with open ("Actions.csv") as file:
        reader = csv.reader(file, delimiter= ",")
        #for row in reader:
            #print(row)

        for i, row in enumerate(reader):
            if i == 0:
                continue
            actions.append(row)
    return actions


gamestate = ["Gamestate", "This is gameState", 999,5,5,5,5,5]
actions = load_actions()

#SimulationLoop
for i in range(100):
    utilities = []
    for action in actions:
        utilities.append(get_utility_score(gamestate, action))

    largest_utility_index =  utilities.index(max(utilities))
    best_action = actions[largest_utility_index]
    gamestate = apply_action(gamestate,best_action)
    print(f"The largest utility index: {largest_utility_index}")
    
    if gamestate[3] <= 0:
        print("Jeeremy is dead beacause of exhaustion")
        break	
    if gamestate[4] <= 0:
        print("Jeeremy is dead beacause of hunger")
        break	
    if gamestate[5] <= 0:
        print("Jeeremy is dead beacause of thirst")
        break
    if gamestate[6] <= 0:
        print("Jeeremy is dead beacause of boredom")
        break
    if gamestate[7] <= 0:
        print("Jeremy is broke")
        break
         