import os
from config import *
import psycopg2


class Sudoers:
    def __init__(self):
        self.sudoers, self.super_sudoers = self.get_data()

    def get_data(self):
        if DATABASE_URL_ACTIVE:
            conn = psycopg2.connect(DATABASE_URL)
        else:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
        self.cursor = conn.cursor()

        sudoers = self.cursor.execute("SELECT user_id, name FROM sudoers")
        super_sudoers = self.cursor.execute("SELECT user_id, name FROM super_sudoers")
        return sudoers, super_sudoers
            
    async def is_sudoer(self, user_id: int) -> bool:
        return user_id in self.sudoers

    async def is_super_sudoer(self, user_id: int) -> bool:
        return user_id in self.super_sudoers    