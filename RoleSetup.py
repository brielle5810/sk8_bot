import discord
from discord.ext import commands

class RoleSetup(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("RoleSetup.py is ready!")

    @commands.command()
    async def setup(self, ctx):
        try:
            embed_var = discord.Embed(title="CHOOSE YOUR ROLES!", description=
            "\nReact to this message to assign yourself a role!\n"
                                      "\n⛏️  mind crafters\n"
                                      "🔫  Valorant Gang\n"
                                      "🐉  DnDers\n"
                                      "🎮  EPIC Fortnite Gamers\n"
                                      "🃏  Pokemon TCG Masters\n"
                                      "🧘‍♂️  master meditators\n"
                                      "💪  SHREDDED\n", color=discord.Color.red())

            await ctx.send(embed=embed_var)
        except Exception as e:
            print("Error:", e)

async def setup(client):
    await client.add_cog(RoleSetup(client))
