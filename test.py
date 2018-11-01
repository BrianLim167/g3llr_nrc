##from nrc import *
##
##abort()
##
##usr = input("Please type your NYU net ID: ")
##nrc = NRC(usr)
##try:
##    nrc.login(input("Choose a benchmark [a,b,c]:"))
##    print("Press ^C at any time to stop")
##    while( input() != "quit"):
##        exec(s)
##except:
##    nrc.reset()
##nrc.reset()
##        

from nrc import *

abort()

usr = input("Please type your NYU net ID: ")
test = NRC(usr)
try:
    s = test.secret
    test.login("a")
    print("Press ^C at any time to stop")
    found = False
    while not found:
        status = test.get_status().json()
        heal_info = test.attempt_heal().json()
        if not "Error" in heal_info:
            solution = NRC.disease_solver(heal_info["Challenge"])
            test.heal_solution(str(solution))
        test.tick()
        if status["number_of_options"] > 1:
            test.select_direction(input("Choose direction {}:".format(status["options"])))
except Exception as e:
    print("########~~ERROR~~########")
    print(e)
    print("########~~ERROR~~########")
    test.reset()
test.reset()
