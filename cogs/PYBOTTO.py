import discord
from discord.ext import commands

class Pybotto(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # Any function in a CogClass must take Self!
    async def on_ready(self):
        print("Pybotto ready!")

    @commands.command()
    async def donators(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def info(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def invite(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def locale(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def perms(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    #Ping/Pong
    async def ping(ctx):
        await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

    @commands.command()
    async def prefix(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def pro(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def settings(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def support(self, ctx):
        await ctx.send(f"Bong!")

def setup(client):
    client.add_cog(Pybotto(client))
