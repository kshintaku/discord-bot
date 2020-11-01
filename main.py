import discord
import os

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!Compile"):
        for x in client.get_all_channels():
            if x.name == "general-text":
                print(x.id)
                channel = client.get_channel(x.id)
                messages = await channel.history(limit=200).flatten()
                messages.reverse()
                strings = []
                for message in messages:
                    strings.append(message.content)
                print(*strings)


client.run(os.environ.get("DISCORD_KEY"))
