import asyncio
import discord
import os
from discord.ext import commands
from discord.utils import get
import bot


def run_discord_bot():
    TOKEN = 'TOKEN'
    client = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    async def load():
        for filename in os.listdir("./cogs"):
            if filename.endswith(".py"):
                await client.load_extension(f"cogs.{filename[:-3]}")
                print(f"{filename[:-3]} is loaded!") #-.py

    @client.event
    async def on_ready():
        for guild in client.guilds:
            for text_ch in guild.text_channels:
                if str(text_ch).strip() == "roles":
                    global verified_id
                    verified_id = text_ch.id
                    break

    @client.event
    async def on_raw_reaction_add(reaction):
        if reaction.channel_id == verified_id:
            if reaction.message_id== MESSAGEID: #id here
                if str(reaction.emoji) == "🔫":
                    verified_role = get(reaction.member.guild.roles, name="Valorant Gang")
                elif str(reaction.emoji) == "🃏":
                    verified_role = get(reaction.member.guild.roles, name="Pokemon TCG Masters")
                elif str(reaction.emoji) == "🐉": #done
                    verified_role = get(reaction.member.guild.roles, name="DnDers")
                elif str(reaction.emoji) == "🎮":
                    verified_role = get(reaction.member.guild.roles, name="EPIC Fortnite Gamers")
                elif str(reaction.emoji) == "⛏️":
                    verified_role = get(reaction.member.guild.roles, name="mind crafters")
                elif str(reaction.emoji) == "🧘‍♂️":
                    verified_role = get(reaction.member.guild.roles, name="master meditators")
                elif str(reaction.emoji) == "💪":
                    verified_role = get(reaction.member.guild.roles, name="SHREDDED")
                elif str(reaction.emoji) == "❤️":
                    verified_role = get(reaction.member.guild.roles, name="verified")
                await reaction.member.add_roles(verified_role)
            #🔫 🐉 🎮 ⛏️ 🃏 🧘‍♂️ 💪

    @client.event
    async def on_raw_reaction_remove(reaction):
        if reaction.message_id == 1138899007960260679:
            guild_id = reaction.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, client.guilds)
            if str(reaction.emoji) == "❤️":
                unverified_role= discord.utils.get(guild.roles,name="verified")
            elif str(reaction.emoji) == "🐉":
                unverified_role = discord.utils.get(guild.roles, name="DnDers")
            elif str(reaction.emoji) == "💪":
                unverified_role = discord.utils.get(guild.roles, name="SHREDDED")
            elif str(reaction.emoji) == "⛏️":
                unverified_role = discord.utils.get(guild.roles, name="mind crafters")
            elif str(reaction.emoji) == "🔫":
                unverified_role = discord.utils.get(guild.roles, name="EPIC Fortnite Gamers")
            elif str(reaction.emoji) == "🧘‍♂️":
                unverified_role = discord.utils.get(guild.roles, name="master meditators")
            elif str(reaction.emoji) == "🃏️":
                unverified_role = discord.utils.get(guild.roles, name="Pokemon TCG Masters")
            elif str(reaction.emoji) == "🔫":
                unverified_role = discord.utils.get(guild.roles, name="Valorant Gang")
            if unverified_role != None:
                member= discord.utils.find(lambda m: m.id ==reaction.user_id, guild.members)
                if member != None:
                    await member.remove_roles(unverified_role)
                else:
                    print("who?")

    async def main_start():
        async with client:
            await load()
            await client.start(TOKEN)

    asyncio.run(main_start())
