import os

class Sudoers:
    def __init__(self):
        self.sudoers = [int(x) for x in os.getenv("SUDOERS", "").split(",") if x.strip().isdigit()] 
        self.sudo_mode = os.getenv("SUDO_MODE", "False").lower() == "true"
        self.super_sudoers = [int(x) for x in os.getenv("SUPER_SUDOERS", "").split(",") if x.strip().isdigit()]

    async def is_sudoer(self, user_id: int) -> bool:
        return user_id in self.sudoers

    async def is_super_sudoer(self, user_id: int) -> bool:
        return user_id in self.super_sudoers    