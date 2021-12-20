import discord
import requests

from resources.channels import Channels

MEME_API_URL = "https://meme-api.herokuapp.com/gimme"

class Meme(discord.ext.commands.Cog, name='Meme module'):
    def __init__(self, bot):
        self.bot = bot

    @discord.ext.commands.command(name="meme")
    async def meme(self, ctx, subreddit = None):
        channel = self.bot.get_channel(Channels.FANTASY)

        request = MEME_API_URL if subreddit is None else f"{MEME_API_URL}/{subreddit}"
        response = await requests.get(request)

        await channel.send(response.url if response.nsfw or response.spoiler else f"||{response.url}||")