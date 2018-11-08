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
    a.login("b")
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
            if True or len(status["options"]) > 1:
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

benchmark()
abort()
        
##except Exception as e:
##    print("########~~ERROR~~########")
##    print(e)
##    print("########~~ERROR~~########")
##    a.reset()
##a.reset()


