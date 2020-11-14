# imports
import discord
from discord.ext import commands
import json
from pathlib import Path
import os

# opening the config file
with open("./config.json") as jsonfile:
    config = json.load(jsonfile)


class speak(commands.Cog):
    def __init__(self, client):
        self.client = client


    # request to speak command
    @commands.command()
    async def speak(self, ctx):
        
        # look in the id file to check 
        IDFileCheck = Path("./id.txt")
        if IDFileCheck.is_file():  
            ErrorEmbed = discord.Embed(
                colour = discord.Colour.light_gray()
            )
            ErrorEmbed.set_author(name = "Another user has requested to speak, please try again later")
            await ctx.send(ctx.author.mention, embed = ErrorEmbed)
        
        else:
            GameOwnerRole = ctx.guild.get_role(config["GameOwnerRole"])
            
            SpeakRequestEmbed = discord.Embed(
                colour = discord.Colour.light_gray(),
                description = "Use the reaction to accept or decline the speaking request"
            )
            SpeakRequestEmbed.set_author(name = f"{ctx.message.author} has requested to speak")
            
            message = await ctx.send(GameOwnerRole.mention, embed = SpeakRequestEmbed)
            
            IDFile = open("./id.txt", "w")
            IDFile.writelines(f"{str(message.id)}\n{str(ctx.author.id)}")
            IDFile.close()

            await message.add_reaction("✅")
            await message.add_reaction("⛔")


    # listening for reactions on the embed and acting on them if they are needed
    @commands.Cog.listener()
    async def on_reaction_add(self, ctx, user):
        
        # getting the info from the text file
        IDFile = open("./id.txt", "r")
        LastMessageID = int(IDFile.readline())
        SpeakerID = int(IDFile.readline())
        IDFile.close()

        

        # checking that the message is the correct on and that the reaction is not from the bot
        if user.id != self.client.user.id and ctx.message.id == LastMessageID :
            # getting the member object for the user that has requested to speak
            Speaker = user.guild.get_member(SpeakerID)
            
            GameOwnerRole = ctx.guild.get_role(config["GameOwnerRole"])

            if GameOwnerRole in user.roles:

                # allowing the user to speak
                if str(ctx) == "✅":
                    await Speaker.edit(mute = False)
                    NowSpeakingEmbed = discord.Embed(
                        colour = discord.Colour.light_gray()
                    )
                    NowSpeakingEmbed.set_author(name = f"{Speaker} is now allowed to speak")
                    await ctx.message.channel.send(embed = NowSpeakingEmbed)
                    await ctx.message.delete()
                    os.remove("./id.txt")
                
                # not allowing the user to speak
                elif str(ctx) == "⛔":
                    NowSpeakingEmbed = discord.Embed(
                        colour = discord.Colour.light_gray()
                    )
                    NowSpeakingEmbed.set_author(name = f"{Speaker}'s request to speak has been declined")
                    await ctx.message.channel.send(embed = NowSpeakingEmbed)
                    await ctx.message.delete()
                    os.remove("./id.txt")

                # the user has not used the correct emojis to react - produces error message
                else:
                    ErrorEmbed = discord.Embed(
                        colour = discord.Colour.light_gray()
                    )
                    ErrorEmbed.set_author(name = f"'{ctx}' is not a recognised reaction. Please react with ✅ or ⛔")
                    await ctx.send(embed = ErrorEmbed)
            
            else:
                ErrorEmbed = discord.Embed(
                    colour = discord.Colour.light_gray()
                )
                ErrorEmbed.set_author(name = "You cannot approve this speak request, only the game owner can")
                await ctx.send(ctx.author.mention, embed = ErrorEmbed)


def setup(client):
    client.add_cog(speak(client))