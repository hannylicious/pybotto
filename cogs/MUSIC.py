import discord
from discord.ext import commands

class Music(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # Any function in a CogClass must take Self!
    async def on_ready(self):
        print("Music ready!")

    @commands.command()
    async def music(self, ctx):
        await ctx.send(f"We will have music!!")

def setup(client):
    client.add_cog(Music(client))
