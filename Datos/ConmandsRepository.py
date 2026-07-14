from Entidad.commands  import ConmandInfo
from config import LANGUAGE
class ComandsRepository:
    def __init__(self):
        self.comands_en = [
            ConmandInfo("help", "Show this help", True, False),
            ConmandInfo("alive", "Check if the bot is alive", True, False),
            ConmandInfo("sudoers", "List sudoers and super sudoers", True, True),
        ]
        self.comands_es = [
            ConmandInfo("help", "Muestra esta ayuda", True, False),
            ConmandInfo("alive", "Verifica si el bot está activo", True, False),
            ConmandInfo("sudoers", "Lista de sudoers y super sudoers", True, True),
        ]
        self.comands_de = [
            ConmandInfo("help", "Zeigt diese Hilfe an", True, False),
            ConmandInfo("alive", "Überprüft, ob der Bot aktiv ist", True, False),
            ConmandInfo("sudoers", "Liste der Sudoers und Super Sudoers", True, True),
        ]
        
    def show_all(self) -> list[ConmandInfo]:
        if LANGUAGE == "es":
            return self.comands_es
        elif LANGUAGE == "de":
            return self.comands_de
        else:
            return self.comands_en
