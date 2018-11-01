from nrc import *

abort()

usr = input("Please type your NYU net ID: ")
a = NRC(usr)
try:
    s = a.secret
    a.login()
    print("Press ^C at any time to stop")
    path = []
    explored = []
    path.append(a.get_status().json()["player_position"])
    while len(path) > 0:
        neighbors = a.get_status().json()["options"]
        deadend = True
        i = 0
        while i < len(neighbors) and deadend:
            if neighbors[i] not in explored:
                deadend = False
                direction = i
        if deadend:
            path.pop()
            a.reset()
            for i in range(len(path)):
                options = a.get_status().json()["options"]
                node = path[i]
                for j in range(len(options)):
                    if node == options[j]:
                        a.select_direction(j)
                a.tick()
        else:
            a.select_direction()
            explored.append(a.getstatus().json()["player_position"])
            path.append(a.getstatus().json()["player_position"])
            a.tick()
except Exception as e:
    print("########~~ERROR~~########")
    print(e)
    print("########~~ERROR~~########")
    test.reset()
test.reset()
