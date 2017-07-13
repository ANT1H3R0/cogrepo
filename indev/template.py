from discord.ext import commands
import discord
from .utils import checks

class Template:
    """Cog Description Here"""

    def __init__(self, bot):
        self.bot = bot

    #Code goes here

def setup(bot):
    bot.add_cog(Template(bot))