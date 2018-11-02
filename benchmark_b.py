from nrc import *

abort()


usr = input("Please type your NYU net ID: ")
a = NRC(usr)
##try:
if True:
    s = a.secret
    a.login("b")
    cured_diseases = 0
    found_brain = False
    pathfind = NRC.pathfinding("BrainR_0")
    while not found_brain:
        status = a.get_status().json()
        heal = a.heal()
        if not "Error" in heal.json():
            print("!!!!!!DISEASE FOUND!!!!!!")
        direction = 0
        minimum = float("inf")
        for i in range(len(status["options"])):
            if status["options"][i] in pathfind and pathfind[status["options"][i]] < minimum:
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
            if status["options"][i] in pathfind and pathfind[status["options"][i]] < minimum:
                minimum = pathfind[status["options"][i]]
                direction = i
        a.select_direction(direction)
        a.tick()
    found_stomach = False
    pathfind = NRC.pathfinding("Stomach_0")
    while not found_stomach:
        status = a.get_status().json()
        heal = a.heal()
        if not "Error" in heal.json():
            print("!!!!!!DISEASE FOUND!!!!!!")
        direction = 0
        minimum = float("inf")
        for i in range(len(status["options"])):
            if status["options"][i] in pathfind and pathfind[status["options"][i]] < minimum:
                minimum = pathfind[status["options"][i]]
                direction = i
        a.select_direction(direction)
        a.tick()
    for i in range(5):
        status = a.get_status().json()
        heal = a.heal()
        if not "Error" in heal.json():
            print("!!!!!!DISEASE FOUND!!!!!!")
        a.tick()
        
##except Exception as e:
##    print("########~~ERROR~~########")
##    print(e)
##    print("########~~ERROR~~########")
##    a.reset()
##a.reset()


