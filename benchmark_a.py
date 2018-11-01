from nrc import *

abort()

usr = input("Please type your NYU net ID: ")
a = NRC(usr, 1)
try:
    s = a.secret
    a.login("a")
    print("Press ^C at any time to stop")
    holds = 0
    turns = 0
    while(holds < 3):
        moves = 0
        while(moves < 8):
            status = a.get_status().json()
            show_pos(status)
            if(status["number_of_options"]>1):
                dir_confirm = a.select_direction(turns)
                print(dir_confirm.text)
                turns+=1
            a.tick()
            moves+=1
        a.start_holding()
        ticks=0
        while(ticks<4):
            a.tick()
            status = a.get_status().json()
            show_pos(status)
            ticks+=1
        a.stop_holding()
        holds+=1
    while(turns< 3):
        status = a.get_status().json()
        show_pos(status)
        if(status["number_of_options"]>1):
            a.select_direction(turns)
            turns+=1
        a.tick()
except Exception as e:
    print("########~~ERROR~~########")
    print(e)
    print("########~~ERROR~~########")
    test.reset()
test.reset()

