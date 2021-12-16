import discord
import random

from resources.happyhour import HappyHour

LOCATIONS = [
    "Pub 42",
    "Manning’s",
    "Como Tap",
    "Outtakes",
    "Scullers’s",
    "Tony Jaros River Garden",
    "Broken Clock Brewing",
    "Park Tavern",
    "Town Hall",
    "Mortimer’s",
    "Bunny’s Bar and Grill",
    "New Bohemia",
    "Pocket Square",
    "Wicked Wort",
    "Utepils"
]

class HappyHour(discord.ext.commands.Cog, name='HappyHour module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="hhrandom")
    async def adhoc_play(self, ctx):
        pick = random.choice(LOCATIONS)
        await ctx.send(f'Hey, you should go to **{pick}**, and remember, Mr.Favor loves you.')