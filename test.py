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
a = NRC(usr)
try:
    s = a.secret
    a.login("a")
    print("Press ^C at any time to stop")
    found = False
    while not found:
        status = a.get_status().json()
        a.attempt_heal()
        a.heal_solution("yes")
        a.tick()
        if status["number_of_options"] > 1:
            a.select_direction(input("Choose direction {}:".format(status["options"])))
except:
    a.reset()
a.reset()

