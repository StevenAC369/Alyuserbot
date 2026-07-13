from telethon import TelegramClient
from config import API_ID, API_HASH, SESSION, HANDLER
from telethon.sessions import StringSession


from Negocios.HelpService import HelpService
from Negocios.AliveService import AliveService

from Vista import Help
from Vista import Alive 

client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)


# This objects verifity rules
help_service = HelpService()
alive_service = AliveService()


comands_help = help_service.command_repo.show_all()

help_run = Help.help_handler(client, HANDLER, comands_help, help_service)
alive_run = Alive.alive_handler(client, HANDLER, alive_service.message, help_service)

if __name__ == "__main__":
    with client:
        print("Alyserbot is running...")
        client.run_until_disconnected()