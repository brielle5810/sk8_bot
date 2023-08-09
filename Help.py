import discord
import bot
from discord.ext import commands
import requests
import json

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Help.py is ready!")

    @commands.command()
    async def help(self, ctx):
        spiel="**Here's a list of commands that sk8bot supports:**\n\n"\
              "**!help : **gives a list of supported commands\n"\
              "**!inspire : **shares an inspirational quote\n"\
              "**!funfact : **returns a fun fact\n" \
              "**!joke : **tells a joke\n" \
              "**!ping : **returns the bot ping in milliseconds\n"\
              "**!animerec {genre}: **given a specific genre, will return a random anime from AniList of that genre\n"\
              "**!genres : **gives a list of genres that will work with !animerec {genre}\n"\
              "**!recme : **returns a random anime recommendation written by MyAnimeList users"

        embed_var = discord.Embed(title="welcome sk8ters!",description= spiel,color=discord.Color.red())
        await ctx.send(embed=embed_var)


async def setup(client):
    client.remove_command('help')
    await client.add_cog(Help(client))
