from core.loader import Module, command

class ExampleModule(Module):
    name = "Example"
    description = "Example"
    version = "1.0.0"
    author = "Userbot"
    
    @command(doc="Say hello")
    async def hello_cmd(self, event):
        await event.edit("Hello!")
    
    @command(doc="Send voice message")
    async def voice_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        
        await self.client.send_file(
            event.chat_id,
            "https://t.me/radiofmonline/195",
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command(doc="Echo message")
    async def echo_cmd(self, event):
        args = event.pattern_match.group(1)
        if not args:
            await event.edit("use: `.echo <text>`")
            return
        
        await event.edit(f"🔊 {args}")
