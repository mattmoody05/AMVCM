# imports
import discord
from discord.ext import commands
import os

class done(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands here
    @commands.command()
    async def done(self, ctx):
        await ctx.author.edit(mute = True)
        
        DoneEmbed = discord.Embed(
            colour = discord.Colour.light_gray()
        )
        DoneEmbed.set_author(name = "You have now be re-muted")
        await ctx.send(ctx.author.mention, embed = DoneEmbed)

        os.remove("./id.txt")
        

def setup(client):
    client.add_cog(done(client))