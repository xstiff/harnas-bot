import discord
import asyncio
from discord.ext import commands
import random



class Poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if message.content.startswith("ankieta:") or message.content.startswith("ankieta") or message.content.startswith("ankieta ") or message.content.startswith("poll:") or message.content.startswith("poll") or message.content.startswith("poll "):
                await message.add_reaction('👍')
                await message.add_reaction('👎')
                await message.add_reaction('🤷')

def setup(bot):
    bot.add_cog(Poll(bot))
    print("poll.py | Loaded \n")