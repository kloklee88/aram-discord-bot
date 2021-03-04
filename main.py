import discord
import os
import random
from keep_alive import keep_alive

keep_alive()

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!aram'):
      command = message.content.strip()
      if len(command.split(' ')) == 2:
        aram_command = command.split(' ')[1]
        if aram_command == 'kevin':
          await message.channel.send('Kevin is awesome!')
        elif aram_command == 'about':
          await message.channel.send('Randomly selects champions split into 2 teams for ARAM inhouses to simulate re-rolls. Made by yours truly, Kevin :)')
        elif aram_command == 'help':
          help_message = 'Commands:\n!aram -- will default to 15 champions for each team\n!aram # -- where # is the number of champions per team, up to a max of 30'
          await message.channel.send(help_message)
        else:
          try:
            number_champions = int(aram_command)
            await message.channel.send(get_balanced_team(number_champions))
          except:
            await message.channel.send('Number of champions is not a number')
      else:
        await message.channel.send(get_balanced_team(15))

champions = ['Aatrox','Ahri','Akali','Alistar','Amumu','Anivia','Annie','Aphelios','Ashe','AurelionSol','Azir','Bard','Blitzcrank','Brand','Braum','Caitlyn','Camille','Cassiopeia','ChoGath','Corki','Darius','Diana','DrMundo','Draven','Ekko','Elise','Evelynn','Ezreal','Fiddlesticks','Fiora','Fizz','Galio','Gangplank','Garen','Gnar','Gragas','Graves','Hecarim','Heimerdinger','Illaoi','Irelia','Ivern','Janna','JarvanIV','Jax','Jayce','Jhin','Jinx','KaiSa','Kalista','Karma','Karthus','Kassadin','Katarina','Kayle','Kayn','Kennen','KhaZix','Kindred','Kled','KogMaw','LeBlanc','LeeSin','Leona','Lissandra','Lucian','Lulu','Lux','Malphite','Malzahar','Maokai','MasterYi','MissFortune','Mordekaiser','Morgana','Nami','Nasus','Nautilus','Neeko','Nidalee','Nocturne','Nunu','Olaf','Orianna','Ornn','Pantheon','Poppy','Pyke','Qiyana','Quinn','Rakan','Rammus','RekSai','Renekton','Rengar','Riven','Rumble','Ryze','Sejuani','Senna','Sett','Shaco','Shen','Shyvana','Singed','Sion','Sivir','Skarner','Sona','Soraka','Swain','Sylas','Syndra','TahmKench','Taliyah','Talon','Taric','Teemo','Thresh','Tristana','Trundle','Tryndamere','TwistedFate','Twitch','Udyr','Urgot','Varus','Vayne','Veigar','VelKoz','Vi','Viktor','Vladimir','Volibear','Warwick','Wukong','Xayah','Xerath','XinZhao','Yasuo','Yorick','Yuumi','Zac','Zed','Ziggs','Zilean','Zoe','Zyra','Lillia','Yone','Seraphine','Rell','Viego']

def random_aram(number_champs):
    if number_champs > 30:
        number_champs = 30
    random.shuffle(champions)
    team_one = champions[0:number_champs]
    team_two = champions[number_champs+1:number_champs+number_champs+1]
    balanced_team = [team_one, team_two]
    return balanced_team

def get_balanced_team(number_champs):
    balanced_team = random_aram(number_champs)
    result = '**Team One:**\n'
    for champ in balanced_team[0]:
        result += champ + '\n'
    result += '\n**Team Two:**\n'
    for champ in balanced_team[1]:
        result += champ + '\n'
    return result

client.run(os.getenv('TOKEN'))