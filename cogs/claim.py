# imports
import discord
from discord.ext import commands
import json
import os
from pathlib import Path

# opening the config file
with open("./config.json") as jsonfile:
    config = json.load(jsonfile)


class claim(commands.Cog):
    def __init__(self, client):
        self.client = client

    # claim command
    @commands.command()
    async def claim(self, ctx, arg):
        
        CodeFileCheck = Path("./code.txt")
        if CodeFileCheck.is_file(): 
            ErrorEmbed = discord.Embed(
                colour = discord.Colour.light_gray()
            )
            ErrorEmbed.set_author(name = "There is already a game in progress, if you think this is false, please contact an admin")

        else:
            # writing the game code to a text file for later reference
            CodeFile = open("./code.txt", "w")
            CodeFile.writelines(arg)
            CodeFile.close()

            # adding the game owner role to the author
            await ctx.author.add_roles(ctx.guild.get_role(config["GameOwnerRole"]))

            # sending an embed to confirm the game has been claimed
            GameClaimEmbed = discord.Embed(
                colour = discord.Colour.light_gray()
            )
            GameClaimEmbed.set_author(name = f"Your game has been claimed with the code '{arg}'")
            await ctx.send(embed = GameClaimEmbed)

            # updating the bot's activity with the code
            await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Among Us | {arg}"))


    # close command
    @commands.command()
    async def close(self, ctx):
        GameOwnerRole = ctx.guild.get_role(config["GameOwnerRole"])
        
        if GameOwnerRole in ctx.author.roles:
            await self.client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="Among Us"))
            await ctx.author.remove_roles(GameOwnerRole)
            os.remove("./code.txt")

            ConfirmEmbed = discord.Embed(
                colour = discord.Colour.light_gray()
            )
            ConfirmEmbed.set_author(name = "Your game has been closed")
            await ctx.send(embed = ConfirmEmbed)

        else:
            GameNotOwnedEmbed = discord.Embed(
                colour = discord.Colour.light_gray()
            )
            GameNotOwnedEmbed.set_author(name = "You do not own a game, therefore you cannot close it")


def setup(client):
    client.add_cog(claim(client))