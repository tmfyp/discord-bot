import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'✅ Бот {bot.user} запущен!')

@bot.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name="ENJOYER")
    if role:
        await member.add_roles(role)
        print(f"Роль {role.name} выдана {member.name}")

bot.run(os.getenv("TOKEN"))
