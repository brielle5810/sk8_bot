import discord
import bot
from discord.ext import commands
import requests
import json
class Joke(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.limit = 1
        self.URL = 'https://api.api-ninjas.com/v1/jokes?limit={}'.format(self.limit)

    @commands.Cog.listener()
    async def on_ready(self):
        print("Joke.py is ready!")

    @commands.command()
    async def joke(self, ctx):
        response = requests.get(self.URL, headers={"X-Api-Key": "YOUR_KEY_HERE"})
        if response.status_code == requests.codes.ok:
            json_data = json.loads(response.text)
            #joke = json_data[0]["joke"]
            embed_var = discord.Embed(title="joke time!", description=json_data[0]["joke"], color=discord.Color.dark_orange())
            await ctx.send(embed=embed_var)

        else:
            print("Error:", response.status_code, response.text)

async def setup(client):
    await client.add_cog(Joke(client))
