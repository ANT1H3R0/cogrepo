from discord.ext import commands
import discord
from .utils import checks

class Firestorm:
    """Initiate Firestorm Protocol."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def firestorm(self, invite: str):
        """Execute command: Firestorm.

        Bans all bannable users and invites them to the specified server."""
        for member in self.bot.get_all_members():
            await self.bot.say(member.mention)

def setup(bot):
    bot.add_cog(Firestorm(bot))