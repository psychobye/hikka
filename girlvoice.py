from core.loader import Module, command

class GirlVoiceModule(Module):
    name = "GirlVoice"
    description = "girl voice messages"
    version = "1.0.0"
    author = "pragmata"

    VOICES = {
        "привет": "https://t.me/radiofmonline/195",
        "кд": "https://t.me/radiofmonline/198",
        "да": "https://t.me/radiofmonline/197",
        "нет": "https://t.me/radiofmonline/196",
        "жаль": "https://t.me/radiofmonline/199",
        "недоверяю": "https://t.me/radiofmonline/200",
        "подожди": "https://t.me/radiofmonline/201",
        "спок": "https://t.me/radiofmonline/202",
        "ясно": "https://t.me/radiofmonline/203",
        "обид": "https://t.me/radiofmonline/204",
        "тмн": "https://t.me/radiofmonline/205",
        "мур": "https://t.me/radiofmonline/206",
        "пж": "https://t.me/radiofmonline/207",
        "спс": "https://t.me/radiofmonline/208",
        "тыгде": "https://t.me/radiofmonline/209",
        "дог": "https://t.me/radiofmonline/210",
        "дутро": "https://t.me/radiofmonline/211",
        "кснемогу": "https://t.me/radiofmonline/212",
        "нипон": "https://t.me/radiofmonline/213",
        "интересно": "https://t.me/radiofmonline/214",
        "чмоки": "https://t.me/radiofmonline/215",
        "спок2": "https://t.me/radiofmonline/216",
        "тыменялюбишь": "https://t.me/radiofmonline/217",
        "нукотик": "https://t.me/radiofmonline/218",
        "котик": "https://t.me/radiofmonline/219",
        "блин": "https://t.me/radiofmonline/220",
        "скоробуду": "https://t.me/radiofmonline/221",
    }
    
    @command()
    async def voice_cmd(self, event):
        args = event.pattern_match.group(1)
        if not args:
            await event.edit("❌ usage: `.voice <name>`")
            return
        
        voice_name = args.strip().lower()
        if voice_name not in self.VOICES:
            await event.edit(f"❌ voice '{voice_name}' not found")
            return
        
        reply = await event.get_reply_message()
        await event.delete()
        
        await self.client.send_file(
            event.chat_id,
            self.VOICES[voice_name],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def привет_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["привет"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def кд_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["кд"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def да_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["да"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def нет_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["нет"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def жаль_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["жаль"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def недоверяю_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["недоверяю"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def подожди_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["подожди"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )

    @command()
    async def спок_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["спок"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def ясно_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["ясно"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def обид_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["обид"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def тмн_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["тмн"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def мур_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["мур"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def пж_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["пж"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def спс_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["спс"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def тыгде_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["тыгде"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def дог_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["дог"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def дутро_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["дутро"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def кснемогу_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["кснемогу"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def нипон_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["нипон"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def интересно_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["интересно"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def чмоки_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["чмоки"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def спок2_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["спок2"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def тыменялюбишь_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["тыменялюбишь"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def нукотик_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["нукотик"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def котик_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["котик"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def блин_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["блин"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
    
    @command()
    async def скоробуду_cmd(self, event):
        reply = await event.get_reply_message()
        await event.delete()
        await self.client.send_file(
            event.chat_id,
            self.VOICES["скоробуду"],
            voice_note=True,
            reply_to=reply.id if reply else None,
        )
