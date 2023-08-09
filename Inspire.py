import discord
import bot
from discord.ext import commands
import requests
import json
class Inspire(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.URL = "https://zenquotes.io/api/random"

    @commands.Cog.listener()
    async def on_ready(self):
        print("Inspire.py is ready!")

    @commands.command()
    async def inspire(self, ctx):
        response = requests.get(self.URL)
        json_data = json.loads(response.text)
        quote = json_data[0]["q"] + " -" + json_data[0]["a"]
        embed_var = discord.Embed(title=json_data[0]["q"],description= f" \- {json_data[0]['a']}",color=discord.Color.dark_teal())
        await ctx.send(embed=embed_var)


async def setup(client):
    await client.add_cog(Inspire(client))
