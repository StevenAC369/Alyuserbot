from telethon import events

def alive_handler(client, handler,message, sudoers):
    @client.on(events.NewMessage(pattern=rf'{handler}alive', outgoing=True))
    async def help_alive(event):
        me = await event.client.get_me()
        if event.sender_id != me.id and event.sender_id not in sudoers.sudoers:
            return 
        await event.edit(message)