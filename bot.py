from config import token
print(token)

import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('/add'):
        parts = message.content.split()
        try:
            num1 = int(parts[1])
            num2 = int(parts[2])
            result = num1 + num2
            await message.channel.send(f'{num1} + {num2} = {result}')
        except (IndexError, ValueError):
            await message.channel.send("Lütfen iki geçerli sayı girin. Örnek: /add 2 2, ayrıca komutta iki sayının arasında + olursa da çalışmaz ve arada boşluk mutlaka olmalıdır...")
client.run(TOKEN)
