from ..Entidad.commands  import ComandInfo

class ComandsRepository:
    def __init__(self):
        self._comands = [
            ComandInfo("help", "Show this help", True, False),
            ComandInfo("alive", "Check if the bot is alive", True, False),
        ]

    def show_all(self) -> list[ComandInfo]:
        return self._comands

