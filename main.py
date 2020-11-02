import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()


description = "Basic python bot with limited functionality to archive channels"

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", description=description, intents=intents)


@bot.event
async def on_ready():
    print("Logging in as")
    print(bot.user.name)
    print(bot.user.id)
    print("________")


@bot.command()
async def compile(ctx, count: int):
    channel = bot.get_channel(ctx.message.channel.id)
    messages = await channel.history(limit=count).flatten()
    messages.reverse()
    strings = []
    for message in messages:
        strings.append(message.content)
    print(*strings)
    await ctx.send("Combined the previous " + str(count) + " messages")


bot.run(os.environ.get("DISCORD_KEY"))
