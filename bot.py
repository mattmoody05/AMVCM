# imports
import discord
from discord.ext import commands
import os
import json

# Opening config.json file
with open("config.json") as jsonfile:
    config = json.load(jsonfile)

# setting up the client object correctly
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix = config["Prefix"], intents=intents)
client.remove_command("help")

# process for when the bot comes online
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Among Us"))
    print(f"\n======= Logged in as {client.user} =======\n")

# process for loading cogs
print("\n======= Loading cogs... =======\n")
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        print(f"Loaded cog: {filename}")

client.run(config["Token"])