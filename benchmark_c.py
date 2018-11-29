from nrc import *
import random

print("hi")
##print(NRC.pathfinding("BrainL_0").items())
##for i in sorted(NRC.pathfinding("BrainL_0").items(), key = lambda i: (i[1],i[0])):
##    print(*i)
abort()

##try:
def benchmark():
##    usr = input("Please type your NYU net ID: ")
    usr = "bl2667"
    a = NRC(usr)
    s = a.secret
    a.login("c")
    
    
    #############################################################################
    ##----------------------------DISEASE--------------------------------------##
    #############################################################################
    diseases_cured = 0
    for organ in ["Heart_0","Stomach_0","BrainL_0"]:
        cured_diseases = 0
        found = False
        pathfind = NRC.pathfinding(organ)
        while not found:
            if "Victory" in a.get_status().text:
                print(a.get_status().text)
                return
            status = a.get_status().json()
            print(status)
            if organ == status["player_position"]:
                found = True
##            print('\n'*80)
            print("--------------------------------------------------------------------")
            print("Current location: "+status["player_position"])
            print("Virus location: "+status["bot_location"])
            print("Finding organ: "+organ)
            print("Diseases cured: "+str(diseases_cured))
            heal = a.heal()
            print(heal.text)
            if not "Error" in heal.text:
                print("!!!!!!DISEASE FOUND!!!!!!")
                time.sleep(5)
                diseases_cured += 1
            else:
                if heal.json()["Error"] != "Not in correct location to cure disease":
                    input()
            print("n  || option")
            print("===||======")
            direction = 0
            minimum = float("inf")
            for i in range(len(status["options"])):
                print((str(pathfind[status["options"][i]])+"  ")[:3]+"|| "+status["options"][i])
                if pathfind[status["options"][i]] < minimum:
                    minimum = pathfind[status["options"][i]]
                    direction = i
            a.select_direction(direction)
            a.tick()
    for i in range(10):
        status = a.get_status().json()
        if "Victory" in a.get_status().text:
            print(a.get_status().text)
            return
##        print('\n'*80)
        print("--------------------------------------------------------------------")
        print("Current location: "+status["player_position"])
        print("Virus location: "+status["bot_location"])
        print("Checking the rest of this organ")
        heal = a.heal()
        print(heal.text)
        if not "Error" in heal.json():
            print("!!!!!!DISEASE FOUND!!!!!!")
            time.sleep(5)
            diseases_cured += 1
        else:
            if heal.json()["Error"] != "Not in correct location to cure disease":
                input()
        a.tick()

    
    #############################################################################
    ##-----------------------------VIRUS---------------------------------------##
    #############################################################################
    while True:
        status = a.get_status().json()
        if "Victory" in a.get_status().text:
            print(a.get_status().text)
            time.sleep(5)
            return
##        print('\n'*80)
        print("--------------------------------------------------------------------")
        print("Current location: "+status["player_position"])
        print("Virus location: "+status["bot_location"])
        virus_distance = ""
        if status["bot_visible"]:
            virus_distance = str(NRC.pathfinding(status["bot_location"])[status["player_position"]])
        print("Virus distance: "+virus_distance)
        print("Visibility: "+str(status["bot_visible"]))
        print("Finding virus")
        if status["number_of_options"] > 1:
            a.start_holding()
##            action = input("Choose action {},{},{},{}:".format(status["options"],"stop","go","abort"))
##            if action == "stop":
##                a.start_holding()
##            elif action == "go":
##                a.stop_holding()
##            elif action == "abort":
##                abort()
##                return
##            else:
##                a.select_direction(action)
        elif status["holding"]:
            a.stop_holding()
##        if status["number_of_options"] > 1:
##            a.select_direction(random.randint(0, status["number_of_options"]-1))
        a.tick()

for i in range(2):
    benchmark()
    abort()

##except Exception as e:
##    print("########~~ERROR~~########")
##    print(e)
##    print("########~~ERROR~~########")
##    a.reset()
##a.reset()
