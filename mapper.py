from nrc import *
import time
import json


##def abort():
##    users = ["abc/abc"]
##    for user in users:
##        s=user
##        r = requests.post(NRC.url_base+"/game/{}/reset".format(s))
##    print(r.text)

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
        is_frontier = False
        while not is_frontier and len(path) > 0:
            for neighbor in nrc_map[path[-1]]:
                if neighbor not in explored:
                    is_frontier = True
            if not is_frontier:
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

for node in nrc_map:
    for neighbor in nrc_map[node]:
        nrc_map[neighbor].append(node)
for node in nrc_map:
    nrc_map[node] = set(nrc_map[node])

fopen = open("map.json", 'w')
fopen.write(json.dumps(nrc_map))
fopen.close()
