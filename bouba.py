import discord

intents = discord.Intents().all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("Le bot est en ligne et prêt à être utilisé.")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!salut"):
        await message.channel.send("Bonjour ! Comment vas-tu ?")

client.run("NzcyNDk0MjAzNjk0NDgxNDQ4.GXYpqe.YTPxhB2aEr8PDlLZ62vgpKNArTNV_0oUyytHl0")
