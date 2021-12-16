import discord
import asyncio
from espn_api.football import League
from datetime import date
from table2ascii import table2ascii as t2a, PresetStyle, Alignment

from resources.channels import Channels

class Scoreboard(discord.ext.commands.Cog, name='Scoreboard module'):
    def __init__(self, bot, league_id, espn_s2, swid):
        self.bot = bot
        self.message = None
        self.league = League(
            league_id=int(league_id), 
            year=int(date.today().year), 
            espn_s2=espn_s2, 
            swid=swid)

    @discord.ext.commands.Cog.listener()
    async def on_ready(self):
        self.message = await self.get_last_bot_message()
        self.bot.loop.create_task(self.scoreboard_task())

    async def scoreboard_task(self):
        while True:
            scoreboard = await self.pretty_scoreboard()
            channel = self.bot.get_channel(Channels.FANTASY)
            if self.message == None:
                self.message = await channel.send(scoreboard)
            else:
                await self.message.edit(content=scoreboard)
            await asyncio.sleep(120)

    async def get_last_bot_message(self):
        channel = self.bot.get_channel(Channels.FANTASY)
        fetchMessage = await channel.history().find(lambda m: m.author.id == self.bot.user.id)
        return fetchMessage

    async def pretty_scoreboard(self):
        current_week = self.league.current_week
        body = []
        max_characters = 12
        for match in self.league.scoreboard():
            current_leader = "TIED"
            home_team_name = (match.home_team.team_name[:max_characters] + '..') if len(match.home_team.team_name) > max_characters else match.home_team.team_name
            away_team_name = ((match.away_team.team_name[:max_characters] + '..') if len(match.away_team.team_name) > max_characters else match.away_team.team_name) if match.away_team else "BYE"
            
            if not match.away_team:
                current_leader = home_team_name
            elif match.home_score > match.away_score:
                current_leader = home_team_name
            elif match.home_score < match.away_score:
                current_leader = away_team_name
            
            body.append([
                home_team_name,
                str(match.home_score) if match.home_score else "0.0",
                away_team_name,
                str(match.away_score) if match.away_score else "0.0",
                current_leader
            ])
        output = t2a(
            header=["Home", "Score", "Away", "Score", "Current Leader"],
            body=body,
            style=PresetStyle.borderless,
            alignments=[Alignment.LEFT,Alignment.LEFT,Alignment.LEFT,Alignment.LEFT,Alignment.LEFT]
        )

        return f"```\nWeek {self.league.current_week} Scoreboard\n\n{output}\n```"
