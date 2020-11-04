# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404

# from .models import Archive
import discord


async def index(request):
    bot = MyBot()
    template = loader.get_template("archive/index.html")
    discord_key = ""
    disc_key = ""
    try:
        discord_key = request.GET.get("code")
    except:
        print("nothing to see here")
    if discord_key:
        # createClient(discord_key)
        bot.start_bot(discord_key)
    context = {
        "discord_key": discord_key,
        "disc_key": disc_key,
    }
    return HttpResponse(template.render(context, request))


async def createClient(discord_key):
    guilds = []
    client = discord.Client()
    client.run(discord_key)
    for x in client.guilds:
        guilds.append(x.name)
    return client


class MyBot:
    def __init__(self):
        self.client = discord.Client()

    async def start_bot(self, key):
        self.client.run(key)

    # @client.event
    async def on_ready(self):
        print(f'{self.client.user} has connected to Discord')
