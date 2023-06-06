from manager import AccountsManager
from messanger import Messanger

# program states
states = {"sign_up" : False, "login" : False,
          "contacts_list" : False, "preferences" : False,
          "messanger" : False}

# main loop
while True:
    if states["sign_up"]:
        AccountsManager.sign_up()
    elif states["login"]:
        AccountsManager.login()
    else:
        pass