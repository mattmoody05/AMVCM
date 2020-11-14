# imports
import discord
from discord.ext import commands

class code(commands.Cog):
    def __init__(self, client):
        self.client = client

    # game code command
    @commands.command()
    async def code (self, ctx):
        CodeFile = open("./code.txt", "r")
        Code = CodeFile.readline()
        CodeFile.close()

        CodeEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        CodeEmbed.set_author(name = f"The code for the game is '{Code}'")
        await ctx.send(embed = CodeEmbed)


def setup(client):
    client.add_cog(code(client))