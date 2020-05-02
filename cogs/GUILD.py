import discord
from discord.ext import commands

class Guild(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    # Any function in a CogClass must take Self!
    async def on_ready(self):
        print("Guild ready!")

    @commands.command()
    async def afk(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def aliases(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def clean(self, ctx):
        await ctx.send(f"Bong!")

    #Clear Channel Chat
    @commands.command()
    async def clear(ctx, amount=5):
        #TODO Look at clearing specific people messages, etc.
        #TODO Make this only accessible by particular people/users/groups
        await ctx.channel.purge(limit=amount)

    #Kick
    @commands.command()
    async def kick(ctx, member : discord.Member, *, reason=None):
        #TODO Limit Access
        await member.kick(reason=reason)
        await ctx.send(f"Kicked {member.mention}")

    #Ban
    @commands.command()
    async def ban(ctx, member : discord.Member, *, reason=None):
        #TODO Limit Access
        await member.ban(reason=reason)
        await ctx.send(f"Banned {member.mention}")

    #Unban
    @commands.command()
    async def unban(ctx, *, member):
        #TODO Limit Access
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split("#")
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f"Unbanned {user.mention}")
                return
            else:
                await ctx.send(f"Cannot unban {member_name}#{member_discriminator}. User not found!")

    @commands.command()
    async def modlog(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def prune(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def rank(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def role(self, ctx):
        await ctx.send(f"Bong!")

    @commands.command()
    async def sar(self, ctx):
        await ctx.send(f"Bong!")

def setup(client):
    client.add_cog(Guild(client))
