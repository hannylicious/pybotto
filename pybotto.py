"Pybotto Discord Bot"
import discord
import random
import os

from discord.ext import commands

TOKEN = os.getenv("PYBOTTO_DISCORD_BOT_TOKEN")

client = commands.Bot(command_prefix = '~')

#Member Joins
@client.event
async def on_member_join(member):
    print(f"{member} has joined a server.")

#Member Leaves
@client.event
async def on_member_remove(member):
    print(f"{member} has left a server.")

#TODO Create various cogs - limit access accordingly

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game("The Great Pybotto!"))
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

#List the files in cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

client.run(TOKEN)
