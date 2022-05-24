import os
import json
import disnake
from disnake.ext import commands, tasks
from dotenv import load_dotenv

from techTreeInfo import *


class StatCommands(commands.Cog):
    """Commands for stat commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="!stats")
    # @commands.cooldown(1, 10, commands.BucketType.user)
    async def statInfo(self, ctx: commands.Context, arg1, arg2=None, arg3=None, arg4=None, arg5=None):
        """
        Command: !stat
        Returns: Redirects user to the !does command due to renaming.
        """

        if arg5 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title() + " " + arg5.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg4 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title() + " " + arg4.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg3 is not None:
            arg1 = arg1.title() + " " + arg2.title() + " " + arg3.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )

        elif arg2 is not None:
            arg1 = arg1.title() + " " + arg2.title()
            try:
                response = techTreeDict[arg1]
            except:
                error = True
                message = disnake.Embed(
                    title="Invalid Input",
                    description="There was a problem with your input. Please check your input and try again.",
                    color=disnake.Color.red(),
                )


        unit_building = unit_building_dict[arg1.title()]
        cost = unit_building["cost"]
        costString = ""

        if cost[0] != 0:
            costString += f"Food: {cost[0]}, "
        if cost[1] != 0:
            costString += f"Wood: {cost[1]}, "
        if cost[2] != 0:
            costString += f"Gold: {cost[2]}, "
        if cost[3] != 0:
            costString += f" Stone: {cost[3]}, "

        if costString != "":
            costString2 = costString[:-2]
        else:
            costString2 = "No resources needed."

        embed = disnake.Embed(title=f"Stats for {arg1}", description=f"Information about {arg1}.", color=0xD5D341)
        embed.add_field(name="Cost", value=costString2, inline=True)
        embed.add_field(name="Attack", value=f"{unit_building['attack']}", inline=True)
        embed.add_field(name="Melee Armor", value=f"{unit_building['melee_armor']}", inline=True)
        embed.add_field(name="Pierce Armor", value=f"{unit_building['pierce_armor']}", inline=True)
        embed.add_field(name="Hit Points", value=f"{unit_building['hit_points']}", inline=True)
        embed.add_field(name="Line of Sight", value=f"{unit_building['los']}", inline=True)
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(StatCommands(bot))
