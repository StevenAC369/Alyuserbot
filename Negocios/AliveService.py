from Datos.messages import messages

class AliveService: 
    def __init__(self):
        self.message = messages.ALIVE_MESSAGE

    def alive_get(self, id_user:int) -> str:
        # validate rules for the user ...
       return self.message