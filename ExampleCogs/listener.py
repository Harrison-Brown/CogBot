from discord.ext import commands

class Listener(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        elif 'keyword' in message.content.lower():
            await message.channel.send('Hello!')
