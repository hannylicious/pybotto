import discord
from discord.ext import commands

class Images(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # Any function in a CogClass must take Self!
    async def on_ready(self):
        print("Images ready!")

    @commands.command()
    async def awoo(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def bad(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def blush(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def confused(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def cuddle(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def dance(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def hug(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def idk(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def insult(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def inu(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def jojo(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def kiss(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def lewd(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def lick(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def neko(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def nom(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def nyan(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def owo(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def pat(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def poke(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def pout(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def slap(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def sleepy(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def smug(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def spongebob(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def stare(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def sumfuk(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def thumbsup(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def triggered(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def waa(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def wasted(self, ctx):
        await ctx.send(f"Bong!")

def setup(client):
    client.add_cog(Images(client))
