import discord

class Greetings(discord.ext.commands.Cog, name='Greetings module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="hey")
    async def adhoc_play(self, ctx):
        await ctx.send(f'Hey {ctx.author.name}, Mr.Favor loves you.')