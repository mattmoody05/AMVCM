# discord imports
import discord
from discord.ext import commands

# embeds
NoCommandFoundEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
NoCommandFoundEmbed.set_author(name="That command could not be found, please try again.")

ArgsErrorEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
ArgsErrorEmbed.set_author(name="You have not provided required arguments. Please try again")

BotPermissionsEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
BotPermissionsEmbed.set_author(name="The bot does not have the relevant permissions to perform this command.")

MemberNotFoundEmbed = discord.Embed(
    colour=discord.Colour.light_gray()
)
MemberNotFoundEmbed.set_author(name="Member not found!")

ForbiddenError = discord.Embed(colour=discord.Colour.light_gray())
ForbiddenError.set_author(name="404 Forbidden Error!")


class Errors(commands.Cog):
    def __init__(self, client):
        self.client = client

    # listening for any errors that occur
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.errors.CommandNotFound):
            """ Command not found error """
            await ctx.send(content=f"{ctx.author.mention}", embed=NoCommandFoundEmbed)

        elif isinstance(error, commands.errors.MissingRequiredArgument):
            """ Missing Required Arguments error """
            await ctx.send(content=f"{ctx.author.mention}", embed=ArgsErrorEmbed)

        elif isinstance(error, commands.errors.BotMissingPermissions):
            """ Bot missing Permissions error """
            await ctx.send(content=f"{ctx.author.mention}", embed=BotPermissionsEmbed)

        elif isinstance(error, commands.errors.MemberNotFound):
            """ Member Not found error """
            await ctx.send(content=f"{ctx.author.mention}", embed=MemberNotFoundEmbed)

        elif isinstance(error, discord.errors.Forbidden):
            """ Discord Forbidden """
            await ctx.send(content=f"{ctx.author.mention}", embed=ForbiddenError)

        else:
            raise error


def setup(client):
    client.add_cog(Errors(client))