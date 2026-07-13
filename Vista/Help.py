from telethon import events

def help_handler(client, handler,comands, sudoers):
    @client.on(events.NewMessage(pattern=rf'{handler}help', outgoing=True))
    async def help_handler(event):
        me = await event.client.get_me()
        if event.sender_id != me.id and event.sender_id not in sudoers.sudoers:
            return  
        

        texto = "**📋 Comandos disponibles:**\n\n"
        for c in comands:
            # etiqueta = " (sudo)" if c.sudo else ""
            texto += f"`.{c.nombre}` —{c.descripcion}\n"
 
        await event.edit(texto)