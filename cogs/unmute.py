# imports
import discord
from discord.ext import commands
import json

# opening the config file
with open("./config.json") as jsonfile:
    config = json.load(jsonfile)


class unmute(commands.Cog):
    def __init__(self, client):
        self.client = client

    # commands here
    @commands.command()
    async def unmute(self, ctx, arg):
        GameOwnerRole = ctx.guild.get_role(config["GameOwnerRole"])

        if GameOwnerRole in ctx.author.roles:
            if arg == "all":
                
                # gets the channel that the person calling the command is currently in
                channel = ctx.author.voice.channel
                
                # gets list of all the members
                members = channel.members
                
                # server muting the members
                for member in members:
                    await member.edit(mute = False)

                # creating and sending an embed to the user confirming that users have been muted
                ConfirmEmbed = discord.Embed(
                    colour = discord.Colour.light_gray()
                )
                ConfirmEmbed.set_author(name = f"{str(len(members))} users have been unmuted")
                await ctx.send(embed = ConfirmEmbed)
            
            else:
                MemberID = int(str(arg).replace("<", "").replace(">", "").replace("@", "").replace("!", ""))
                member = ctx.guild.get_member(MemberID)
                await member.edit(mute = False)

                ConfirmEmbed = discord.Embed(
                    colour = discord.Colour.light_gray()
                )
                ConfirmEmbed.set_author(name = f"{member} has been unmuted")
                await ctx.send(embed = ConfirmEmbed)
        
        else:
            ErrorEmbed = discord.Embed(
                colour = discord.Colour.light_gray()
            )
            ErrorEmbed.set_author(name = "You do not have access to this command")
            await ctx.send(ctx.author.mention, embed = ErrorEmbed)
            

def setup(client):
    client.add_cog(unmute(client))