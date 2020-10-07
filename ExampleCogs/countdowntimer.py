from discord.ext import commands
import datetime


class Timer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief = 'Basic countdown timer',
                      description = 'Will return how much time remains.')
    async def timer(self, ctx):
        d1 = datetime.datetime(2020, 10, 7, hour = 23, minute = 14)
        d3 = datetime.datetime.now()
        d4 = d1 - d3

        hours, remainder = divmod(d4.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        msg = '{} days, {:02} hours, {:02} minutes, and {:02} seconds remain...'.format(d4.days, int(hours), int(minutes), int(seconds))
        await ctx.send(msg)
