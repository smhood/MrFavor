#!/usr/bin/env python3

import os
import json
from dotenv import load_dotenv

import discord
## Clients
from clients.custom_bot import CustomBotClient

## Cogs
from cogs.general.greetings import Greetings
from cogs.general.memes import Memes
from cogs.fantasy.scoreboard import Scoreboard
from cogs.general.happyhour import HappyHour

load_dotenv()

TOKEN = os.environ.get("DISCORD_TOKEN")
COMMAND_PREFIX = os.environ.get("COMMAND_PREFIX")
LEAGUE_ID = os.environ.get("LEAGUE_ID")
ESPN_S2 = os.environ.get("ESPN_S2")
ESPN_SWID = os.environ.get("ESPN_SWID")

def main():
    intents = discord.Intents.default()
    intents.members = True

    bot = CustomBotClient(
        command_prefix=COMMAND_PREFIX, 
        intents=intents
    )

    bot.add_cog(Greetings(bot))
    bot.add_cog(Memes(bot))
    bot.add_cog(Scoreboard(bot, LEAGUE_ID, ESPN_S2, ESPN_SWID))
    bot.add_cog(HappyHour(bot))

    bot.run(TOKEN)


if __name__ == '__main__':
    main()