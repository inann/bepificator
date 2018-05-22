import discord
import asyncio

client = discord.Client()

def check_for_rollers(reaction, user):
    reaction_string = str(reaction.emoji)
    if reaction_string.startswith('✋'):
        return user

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith('$$'):
        message_to_bep = message.content[2:]
        output_message = ''
        for letter in message_to_bep:
            output_message = output_message + ':regional_indicator_' + letter + ':'
        await client.send_message(message.channel, output_message)

client.run('')
