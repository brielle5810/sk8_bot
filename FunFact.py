
import discord
from discord.ext import commands
import requests
import json
class FunFact(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.limit = 1
        self.URL = 'https://api.api-ninjas.com/v1/facts?limit={}'.format(self.limit)

    @commands.Cog.listener()
    async def on_ready(self):
        print("FunFact.py is ready!")


    @commands.command()
    async def funfact(self, ctx):
        response = requests.get(self.URL, headers={"X-Api-Key": "YOUR_KEY_HERE"})
        if response.status_code == requests.codes.ok:
            json_data = json.loads(response.text)
            fact = json_data[0]["fact"]
            embed_var = discord.Embed(title="fun fact: ", description=json_data[0]["fact"], color=discord.Color.dark_magenta())

            await ctx.send(embed=embed_var)
        else:
            print("Error:", response.status_code, response.text)


async def setup(client):
    await client.add_cog(FunFact(client))

