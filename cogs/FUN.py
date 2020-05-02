import discord
from discord.ext import commands

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # Any function in a CogClass must take Self!
    async def on_ready(self):
        print("Fun ready!")

    @commands.command()
    async def bigtext(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def bigtextd(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def f(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def flipcoin(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def fortune(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def lenny(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def lennyd(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def say(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def sayd(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def shrug(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def shrugd(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command(aliases=['8ball'])
    async def _8ball(ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]
        await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

def setup(client):
    client.add_cog(Fun(client))
