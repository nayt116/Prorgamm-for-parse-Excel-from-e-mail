import poplib

class Conection_to_pop:
    def __init__(self, user_name:str, password:str, *, pop_server_name = 'pop3.mail.ru'):
        self.user = user_name
        self.passw_ = password
        self.pop_server_name = pop_server_name
        self.pop_server = poplib.POP3_SSL(self.pop_server_name)


    def connection_to_mail(self):
        try:
            self.pop_server.user(self.user)
            self.pop_server.pass_(self.passw_)
            print('\n[S] [W] ->  The user_name, password is succesful!\n')
        except Exception as ex:
        	print(' <[W]> <[S]> The Error is become mabe <<<<<<<<<< from your password or user_name! >>>>>>>>> ', ex)


    def quit(self):
        self.pop_server.quit()