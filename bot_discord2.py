from email import message
import discord
import os

from tqdm import tqdm 
import time
with tqdm(total=100) as pbar:
    for i in range(4):
        time.sleep(0.5)
        pbar.update(25)


class MyClient(discord.Client):
    async def on_ready(self):
        print('Developed by @andrezin.py')
        print('intagram: https://www.instagram.com/andreison.py/ ')
        print('Funcionando como: {0}!'.format(self.user))

    async def on_message(self, message):
        print('Mensagem de {0.author}:{0.content}'.format(message))
        if message.content == '!regras':
            await message.channel.send(f'@{message.author.name} as regras do servidor são:{os.linesep}:point_right:1. Respeitar todos igualmente.{os.linesep}:point_right:3. Não gritar nas calls.{os.linesep}:point_right: 4. Não enviar pornográfia.{os.linesep}:point_right:5. Não enviar gore.{os.linesep}:point_right:6. Evitar off-topic.{os.linesep}:point_right:7. Usar bot de música somente nos canais de música.{os.linesep}')
        elif message.content == '!nivel':
            await message.author.send('Nivel ainda não foi programado :/')
    async def on_menber_join(self,member):
        guild = member.guild
        if guild.system_channel is not None:
            mensagem = f'{member.mention} acabou de entrar no {guild.name}, seja bem vindo(a)!'
            await guild.system_channel.send(message)
    async def on_message(self, message):
        print('Mensagem de {0.author}: {0.content}'.format(message))
        if message.content == 'oi':
            await message.channel.send(f'Olá {message.author.name}')
    async def on_message(self, message):
        print('Mensagem de {0.author}: {0.content}'.format(message))
        if message.content == 'ola':
            await message.channel.send(f'Olá {message.author.name}')
intents = discord.Intents.default()
intents.members = True
client = MyClient(intents = intents)
client.run('T---OKEN HERE---')
