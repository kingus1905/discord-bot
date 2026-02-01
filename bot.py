import discord
from discord.ext import commands

# Intencje (uprawnienia)
intents = discord.Intents.default()
intents.message_content = True

# Prefix komend (np. !hej)
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot zalogowany jako {bot.user}")

@bot.command()
async def hej(ctx):
    await ctx.send("Hej! 👋 Miło Cię widzieć!")

@bot.command()
async def ping(ctx):
    await ctx.send("Pong 🏓")

# 🔴 TU WKLEJ SWÓJ TOKEN
bot.run(os.getenv("DISCORD_TOKEN"))

