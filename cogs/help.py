# imports
import discord
from discord.ext import commands

# embeds
InfoEmbed = discord.Embed(
    colour = discord.Colour.light_gray()
)
InfoEmbed.set_author(name = "Among Us Voice Channel Control Bot")
InfoEmbed.add_field(name = "Game claiming", value = """**.claim ABCDEF - **claims the among us game using the code provided. The code will be displayed in the bot's status and can be accessed by anyone on the server.
**.close - **Closes the currently in use game. (only the game owner can do this)""")
InfoEmbed.add_field(name = "Game owner commands", value = """**.mute all - **Server mutes all the people that are in your voice channel.
**.unmute all -**Server unmutes all the people that are in your voice channel.""")
InfoEmbed.add_field(name = "Game player commands", value = """**.speak - **Sends a message to the game owner that allows them to approve your speaking request or decline it.
**.done - **Once you have finished speaking, you should use this. You will be muted again after running this.
**.code - **Displays the game code for the game that is currently being played.""")


class info(commands.Cog):
    def __init__(self, client):
        self.client = client

    # info / help command
    @commands.command(name = "info",
                    aliases = ["help"])
    async def info(self, ctx):
        await ctx.send(embed = InfoEmbed)


def setup(client):
    client.add_cog(info(client))