import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.voice_states = True

TOKEN = 'MTEzNzE3MzQ1NzUyMDU2MjI3Nw.G0ey1e.fpPhc5jvJ0KEFH7xhP8kmGDnwaV4TjaUnVcmRw'
GUILD_ID = 712692240543121490
ROLE_ID = 1137144355396784138

bot = commands.Bot(command_prefix='×', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

@bot.event
async def on_voice_state_update(member, before, after):
    if before.channel != after.channel:
        if after.channel:  
            guild = bot.get_guild(GUILD_ID)
            role = guild.get_role(ROLE_ID)
            await member.add_roles(role)
        if before.channel:  
            guild = bot.get_guild(GUILD_ID)
            role = guild.get_role(ROLE_ID)
            await member.remove_roles(role)

bot.run(TOKEN)
