from nrc import *
import time

abort()

usr = input("Please type your NYU net ID: ")
a = NRC(usr)
##try:
s = a.secret
a.login('a')
print("Press ^C at any time to stop")
nrc_map = {}
path = []
explored = []
path.append(a.get_status().json()["player_position"])
while len(path) > 0:
    neighbors = a.get_status().json()["options"]
    here = a.get_status().json()["player_position"]
    nrc_map[here] = neighbors
    print(here)
    print(explored)
    deadend = True
    explored.append(a.get_status().json()["player_position"])
    i = 0
    while i < len(neighbors) and deadend:
        if neighbors[i] not in explored:
            deadend = False
            direction = i
        i += 1
    if deadend:
        path.pop()
        a.reset()
        a = NRC(usr)
        a.login('a')
        for j in range(len(path)):
            options = a.get_status().json()["options"]
            node = path[j]
            for k in range(len(options)):
                if node == options[k]:
                    a.select_direction(k)
            a.tick()
    else:
        path.append(a.get_status().json()["player_position"])
        a.select_direction(direction)
        a.tick()
##except Exception as e:
##    print("########~~ERROR~~########")
##    print(e)
##    print("########~~ERROR~~########")
##    a.reset()
a.reset()

fopen = open("map.json", 'w')
fopen.write(str(nrc_map))
