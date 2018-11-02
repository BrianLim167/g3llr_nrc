from nrc import *

abort()


usr = input("Please type your NYU net ID: ")
a = NRC(usr)
try:
    s = a.secret
    a.login("b")
    cured_diseases = 0
    found_brain = False
    pathfind = NRC.pathfinding("Brain_0")
    while not found_brain:
        status = a.get_status().json()
        heal = a.heal()
        if not "Error" in heal.json():
            print("!!!!!!DISEASE FOUND!!!!!!")
        direction = 0
        minimum = float("inf")
        for i in range(len(status["options"])):
            if pathfind[status["options"][i]] < minimum:
                minimum = pathfind[status["options"][i]]
                direction = i
        a.select_direction(direction)
        a.tick()
    found_heart = False
    pathfind = NRC.pathfinding("Heart_0")
    while not found_heart:
        status = a.get_status().json()
        heal = a.heal()
        if not "Error" in heal.json():
            print("!!!!!!DISEASE FOUND!!!!!!")
        direction = 0
        minimum = float("inf")
        for i in range(len(status["options"])):
            if pathfind[status["options"][i]] < minimum:
                minimum = pathfind[status["options"][i]]
                direction = i
        a.select_direction(direction)
        a.tick()
    found_kidney = False
    pathfind = NRC.pathfinding("Kidney_0")
    while not found_kidney:
        status = a.get_status().json()
        heal = a.heal()
        if not "Error" in heal.json():
            print("!!!!!!DISEASE FOUND!!!!!!")
        direction = 0
        minimum = float("inf")
        for i in range(len(status["options"])):
            if pathfind[status["options"][i]] < minimum:
                minimum = pathfind[status["options"][i]]
                direction = i
        a.select_direction(direction)
        a.tick()
        
except Exception as e:
    print("########~~ERROR~~########")
    print(e)
    print("########~~ERROR~~########")
    a.reset()
a.reset()


