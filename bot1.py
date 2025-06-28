import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Канал для выдачи ролей
TARGET_CHANNEL_ID = 1388234894546702438

@bot.event
async def on_ready():
    print(f'Бот запущен как {bot.user}')

@bot.command()
async def gender(ctx):
    if ctx.channel.id != TARGET_CHANNEL_ID:
        await ctx.send("Эта команда доступна только в специальном канале.")
        return
    
    embed = discord.Embed(
        title="Выберите свой пол",
        description="🍆 — Мужчина\n🍓 — Женщина",
        color=0x00ff00
    )
    message = await ctx.send(embed=embed)
    await message.add_reaction('🍆')
    await message.add_reaction('🍓')

@bot.event
async def on_raw_reaction_add(payload):
    if payload.channel_id != TARGET_CHANNEL_ID:
        return
    
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if member.bot:
        return
    
    if str(payload.emoji) == '🍆':
        role = discord.utils.get(guild.roles, name="Мужчина")
        if role:
            await member.add_roles(role)
            print(f"Выдана роль Мужчина пользователю {member}")
    elif str(payload.emoji) == '🍓':
        role = discord.utils.get(guild.roles, name="Женщина")
        if role:
            await member.add_roles(role)
            print(f"Выдана роль Женщина пользователю {member}")

@bot.event
async def on_raw_reaction_remove(payload):
    if payload.channel_id != TARGET_CHANNEL_ID:
        return
    
    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if member.bot:
        return

    if str(payload.emoji) == '🍆':
        role = discord.utils.get(guild.roles, name="Мужчина")
        if role:
            await member.remove_roles(role)
            print(f"Удалена роль Мужчина у пользователя {member}")
    elif str(payload.emoji) == '🍓':
        role = discord.utils.get(guild.roles, name="Женщина")
        if role:
            await member.remove_roles(role)
            print(f"Удалена роль Женщина у пользователя {member}")

# Запустите бота с вашим токеном
import os
bot.run(os.getenv("DISCORD_TOKEN"))

