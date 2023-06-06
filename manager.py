class AccountsManager:
    def __init__(self):
        pass

    def login(self):
        pass

    def sign_up(self):
        username_complete = False
        password_complete = False
        def input_function(info, user_or_pass):
            if len(info) < 3 or len(info) > 20:
                return "Please enter a username between 3-20 characters"
            elif len(info) > 3 and len(info) < 20:
                user_or_pass = True
            else:
                return "Error, please try again"

        while True:
            if username_complete == False:
                username = str(input("Please enter a username (lowercase):"))
                input_function(username, username_complete)
            elif username_complete:
                password = str(input("Please enter a password:"))
                input_function(password, password_complete)
            else:
                pass
                
            
