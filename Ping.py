import discord
import bot
from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping.py is ready!")

    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        embed_var=discord.Embed(title="PONG!", description=f"{bot_latency} ms.",color=discord.Color.green())
        await ctx.send(embed_var)


async def setup(client):
    await client.add_cog(Ping(client))
