import discord
import json
from discord.ext import commands, tasks

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['token']
GUILD_ID = config['guild_id']
CHANNELS = config['channels']
INTERVAL = config['interval']
VOICE_CHANNEL_ID = int(config['voice_channel_id'])  
intents = discord.Intents.default()
intents.messages = True
intents.voice_states = True  
client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')
    guild = client.get_guild(int(GUILD_ID))
    
    if guild is None:
        print(f"Não consegui encontrar o servidor com o ID {GUILD_ID}.")
        return

    voice_channel = guild.get_channel(VOICE_CHANNEL_ID)
    if voice_channel:
        print(f'Entrando no canal de voz: {voice_channel.name}')
        await voice_channel.connect()  
    else:
        print(f"Não consegui encontrar o canal de voz com ID {VOICE_CHANNEL_ID}.")

    periodic_task.start(guild)

@tasks.loop(seconds=INTERVAL)
async def periodic_task(guild):
    """Função que deleta e recria os canais periodicamente"""
    print(f"Iniciando o ciclo de deletar e recriar canais.")

    for channel_info in CHANNELS:
        channel_name = channel_info['name']
        channel_type = channel_info['type']
        category_name = channel_info['category']
        permissions = channel_info['permissions']
        
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        
        if existing_channel:
            print(f"Deletando canal: {channel_name}")
            
            category = discord.utils.get(guild.categories, name=category_name)
            if permissions:
                perms = existing_channel.overwrites 
                
            await existing_channel.delete()
        if channel_type == 'text':
            new_channel = await guild.create_text_channel(channel_name, category=category)
        elif channel_type == 'voice':
            new_channel = await guild.create_voice_channel(channel_name, category=category)
        
        if permissions:
            for target, overwrite in perms.items():
                await new_channel.set_permissions(target, overwrite=overwrite)

        print(f"Canal '{channel_name}' recriado na categoria '{category_name}'.")

@client.command()
async def reset(ctx):
    """Comando para resetar os canais manualmente"""
    guild = ctx.guild
    if guild is None:
        await ctx.send("Servidor não encontrado.")
        return

    for channel_info in CHANNELS:
        channel_name = channel_info['name']
        channel_type = channel_info['type']
        category_name = channel_info['category']
        permissions = channel_info['permissions']
        
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        
        if existing_channel:
            await existing_channel.delete()
        
        category = discord.utils.get(guild.categories, name=category_name)

        if channel_type == 'text':
            new_channel = await guild.create_text_channel(channel_name, category=category)
        elif channel_type == 'voice':
            new_channel = await guild.create_voice_channel(channel_name, category=category)

        if permissions:
            for target, overwrite in perms.items():
                await new_channel.set_permissions(target, overwrite=overwrite)

    await ctx.send("Canais deletados e recriados com sucesso.")

client.run(TOKEN)
