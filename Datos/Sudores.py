import os

class Sudoers:
    def __init__(self):
        

    async def is_sudoer(self, user_id: int) -> bool:
        return user_id in self.sudoers

    async def is_super_sudoer(self, user_id: int) -> bool:
        return user_id in self.super_sudoers    