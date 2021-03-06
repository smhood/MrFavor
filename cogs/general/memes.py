import discord
import requests

from resources.channels import Channels

MEME_API_URL = "https://meme-api.herokuapp.com/gimme"

class Memes(discord.ext.commands.Cog, name='Meme module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="meme")
    async def meme(self, ctx, subreddit = None):
        request = MEME_API_URL if subreddit is None else f"{MEME_API_URL}/{subreddit}"
        response = requests.get(request)
        meme = response.json()
        
        await ctx.send(f"{ctx.author.mention} heres your meme, and remember... Mr.Favor love you.\n" + meme['url'] if not meme['spoiler'] else f"|| {meme['url']} ||")