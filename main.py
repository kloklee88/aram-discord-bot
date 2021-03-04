import discord
import os
import random
from keep_alive import keep_alive
import replit_db_crud
import requests

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
      print(aram_command)
      if aram_command.startswith('<@!'):
        result = get_personalized_message(message.mentions[0])
        await message.channel.send(result)
      elif aram_command == 'about':
        await message.channel.send('Randomly selects champions split into 2 teams for ARAM inhouses to simulate re-rolls. Made by yours truly, Kevin :)')
      elif aram_command == 'help':
        help_message = 'Commands:\n**!aram** -- will default to 15 champions for each team\n**!aram #** -- where # is the number of champions per team, up to a max of 30\n**!aram total** -- show total number of all currently available champions used by the bot\n**!aram all** -- show all currently available champions\n**!aram update** -- get latest champions from Riot (use when list is out of date)\n**!aram about** -- bot description\n**!aram @mention** -- where @mention is anybody in the server to receive a customized message (maybe)'
        await message.channel.send(help_message)
      elif aram_command == 'all':
        await message.channel.send(', '.join(get_all_champions()))
      elif aram_command == 'total':
        await message.channel.send(len(get_all_champions()))
      elif aram_command == 'update':
        await message.channel.send('Running update... please wait...')
        result = update_champions()
        if result == True:
          await message.channel.send('Champions updated!')
        else:
          await message.channel.send('Error. Champions were not updated.')
      else:
        try:
          number_champions = int(aram_command)
          await message.channel.send(get_balanced_team(number_champions))
        except:
          await message.channel.send('Invalid command')
    else:
      await message.channel.send(get_balanced_team(15))

def random_aram(number_champs):
  champions = get_all_champions()
  if number_champs > 30:
    number_champs = 30
  if number_champs <= 0:
    number_champs = 1
  random.shuffle(champions)
  team_one = champions[0:number_champs]
  team_two = champions[number_champs+1:number_champs+number_champs+1]
  team_one.sort()
  team_two.sort()
  balanced_team = [team_one, team_two]
  print(balanced_team)
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

def get_all_champions():
  return replit_db_crud.get_champs()

def update_champions():
  try:
    response = requests.get('https://ddragon.leagueoflegends.com/cdn/11.5.1/data/en_US/champion.json')
    champ_json = response.json()['data']
    champs = ''
    for key in champ_json.keys():
      champs += champ_json[key]['name'] + ','
    champs = champs[:-1] #remove last comma from string
    replit_db_crud.save_champs(champs)
    return True
  except:
    return False

def get_personalized_message(user):
  name = user.name
  print(name)
  if name == 'Confucius':
    result = 'Kevin is awesome!'
  elif name == 'Not Today':
    result = 'What do we say to the God of Death?||Not Today||'
  elif name == 'xXMadreloaderXx':
    result = 'Hej'
  elif name == 'Rags':
    result = '*Top 50 Ashe!*'
  elif name == 'AGenericName':
    result = 'All-in? $2000?'
  elif name == 'Caroline':
    result = 'Top 2 Locked Camera Player on server - Shurimaaaaaaa *Shuffleeeeeeeeeee*'
  elif name == 'Cheqelz':
    result = 'Cheers!!! :beers:'
  elif name == 'Manoafalls':
    result = '**#1 ARAM Player** :trophy:'
  elif name == 'foghi8':
    result = 'Definitely a ~~MONKEY~~ :monkey_face: good LoL player'
  elif name == 'Eroc':
    result = 'Camile says that `Python is an awesome programming language`'
  elif name == 'Bombogi':
    result = 'Valorant > League'
  elif name == 'Buhyun':
    result = 'TWICE!'
  elif name == 'Tourbear':
    result = 'KC :hearts:'
  elif name == 'ARAM Bot':
    result = 'Well, thank my creator Kevin, heard he is a great dude. :robot:'
  elif name == 'Lsw1225':
    result = 'Warwick is raging'
  elif 'ellie' in name:
    result = 'DJJJJJJJJ ~~Khaled~~ Beth :musical_note:'
  else:
    result = ':smiley:'
  return result

client.run(os.getenv('TOKEN'))