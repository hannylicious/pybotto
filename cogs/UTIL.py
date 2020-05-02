import discord
from discord.ext import commands

class Util(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # Any function in a CogClass must take Self!
    async def on_ready(self):
        print("Utils ready!")

    @commands.command()
    async def avatar(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def botlist(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def channelinfo(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def linkcheck(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def pick(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def random(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def reminder(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def roleinfo(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def rolemembers(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def serverinfo(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def urban(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def userinfo(self, ctx):
        await ctx.send(f"Bong!")

    #Cog (for loading other classes/groups of commands)
    @commands.command()
    async def load(ctx, extension):
        client.load_extension(f"cogs.{extension}")

    #Cog (unloading cog)
    @commands.command()
    async def unload(ctx, extension):
        client.unload_extension(f"cogs.{extension}")

    #Cog (reload)
    @commands.command()
    async def reload(ctx, extension):
        client.unload_extension(f"cogs.{extension}")
        client.load_extension(f"cogs.{extension}")

def setup(client):
    client.add_cog(Util(client))
