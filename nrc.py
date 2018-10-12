import requests
import random
import time

##command_family = "login"
##user = "bl2667"
##secret = "awogo"
##
##test = "http://10.42.0.1:5000/login/bl2667/awogo/"
##r = requests.post(test)
##print(r.text)
##print("done")
##
##r = requests.post("http://10.42.0.1:5000/{}/{}/{}/"\
##                  .format(command_family,user,secret))
##print(r.text,"@@@@@@@@@@")
##
##r = requests.post("http://10.42.0.1:5000/{}/{}/{}/{}/{}"\
##                  .format("game","bl2667",secret,"tick",""))
##print(r.text)

##test = "http://10.42.0.1:5000/game/bl2667/awogo/tick"
##t = requests.post(test)
##print(t.text)
##print("done")
##
##
##test = "http://10.42.0.1:5000/game/bl2667/awogo/reset"
##t = requests.post(test)
##print(t.text)
##print("done")


class LoginError(Exception):
    pass

class NRC(object):
    url_base = "http://10.42.0.1:5000" # start of every URL
    
    def __init__(self, user, delay=0, secret=None):
        if secret == None:
            secret = NRC.gen_secret()

        self.user = user
        self.secret = secret
        self.delay = delay # seconds to wait between each action

    # create a secret string of size n of random letters and numbers
    @staticmethod
    def gen_secret(n=16):
        secret = ""
        
        # list of ascii codes of allowed characters
        char_lst = [i for i in range(ord('z')) if chr(i).isalnum()]
        
        for i in range(n):
            secret += chr(random.choice(char_lst))

        print("Your secret is: {}".format(secret))
        return secret

    # send a POST request
    def post(self, family, *args):
        time.sleep(self.delay)
        url = '/'.join([NRC.url_base, family, self.user, self.secret, *args])
        print(url)
        r = requests.post(url)
        print(r.text)
        if r.text == "Please wait for the current group to finish before attempting to login.":
            raise LoginError
##        print("done")
        return r

    # send a GET request
    def get(self, family, *args):
        time.sleep(self.delay)
        url = '/'.join([NRC.url_base, family, self.user, self.secret, *args])
        print(url)
        r = requests.get(url)
        print(r.text)
##        print("done")
        return r

    def login(self):
        return self.post("login")

    def tick(self):
        return self.post("game", "tick")

    def start_holding(self):
        return self.post("game", "start_holding")

    def stop_holding(self):
        return self.post("game", "stop_holding")

    def select_direction(self, index):
        return self.post("game", "select_direction", str(index))

    def reset(self):
        return self.post("game", "reset")

    def get_status(self):
        return self.get("game", "get_status")

# TESTING
usr = input("Please type your NYU net ID: ")
a = NRC(usr)
s = a.secret
a.login()
a.tick()
a.start_holding()
a.tick()
a.stop_holding()
a.tick()
a.select_direction(1)
a.tick()
a.get_status()
a.reset()
