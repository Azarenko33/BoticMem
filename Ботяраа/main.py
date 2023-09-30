import discord
from discord.ext import commands
import os
import random
import requests

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Вы вошли как - {bot.user}')

@bot.command()
async def mem(ctx):
    files = os.listdir('images')
    random_file = random.choice(files)
    file_path = os.path.join('images', random_file)
    
    with open(file_path, 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def joke(ctx):
    # Используем API для получения случайной шутки
    response = requests.get('https://v2.jokeapi.dev/joke/Any')
    
    if response.status_code == 200:
        data = response.json()
        if 'joke' in data:
            await ctx.send(data['joke'])
        elif 'setup' in data and 'delivery' in data:
            await ctx.send(f"{data['setup']}\n*{data['delivery']}*")
        else:
            await ctx.send('Не удалось получить шутку :( .')
    else:
        await ctx.send('О нет, произошла ошибка с получением шутки :(.')

bot.run("Токен бота")