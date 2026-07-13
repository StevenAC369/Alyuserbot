from Entidad.commands import ConmandInfo
from Datos.ConmandsRepository import ComandsRepository

class HelpService: 
    def __init__(self):
        self.command_repo = ComandsRepository()

    def help_get(self, id_user:int) -> list[ConmandInfo]:
        conmands_list = self.command_repo.show_all()
        
        # Filter commands for super sudo users
        # if super_sudo:
        #    conmands_list = [conmand for conmand in conmands_list if conmand.super_sudo]
        return conmands_list