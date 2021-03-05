import discord
import os
import aram_service
from keep_alive import keep_alive

#Flask Server to keep repl.it alive
keep_alive()

client = discord.Client()

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return

  #Process message commands
  if message.content.startswith('!aram'):
    command = message.content.strip()
    if len(command.split(' ')) == 2:
      aram_command = command.split(' ')[1]
      if aram_command.startswith('<@!'):
        await message.channel.send(personalized_message(message))
      elif aram_command == 'about':
        await message.channel.send(about(message))
      elif aram_command == 'help':
        await message.channel.send(help(message))
      elif aram_command == 'all':
        await message.channel.send(all(message))
      elif aram_command == 'total':
        await message.channel.send(total(message))
      elif aram_command == 'update':
        await message.channel.send('Running update... please wait...')
        await message.channel.send(update(message))
      elif aram_command == 'lastletter':
        await message.channel.send(last_letter(message))
      else:
        await message.channel.send(aram_number(message,aram_command))
    else:
      await message.channel.send(aram_default(message))

def personalized_message(message):
  return aram_service.get_personalized_message(message.mentions[0])

def about(message):
  return 'Randomly selects champions split into 2 teams for ARAM inhouses to simulate re-rolls. Made by yours truly, Kevin :)'

def help(message):
  return 'Commands:\n**!aram** -- will default to 15 champions for each team\n**!aram #** -- where # is the number of champions per team, up to a max of 30\n**!aram total** -- show total number of all currently available champions used by the bot\n**!aram all** -- show all currently available champions\n**!aram update** -- get latest champions from Riot (use when list is out of date)\n**!aram about** -- bot description\n**!aram @mention** -- where @mention is anybody in the server to receive a customized message (maybe)'

def all(message):
  return ', '.join(aram_service.get_all_champions())

def total(message):
  return len(aram_service.get_all_champions())

def update(message):
  result = aram_service.update_champions()
  if result == True:
    return 'Champions updated!'
  else:
    return 'Error. Champions were not updated.'

def last_letter(message):
  return aram_service.get_balanced_team(int(15), 'lastletter')

def aram_number(message, aram_command):
  try:
    number_champions = int(aram_command)
    return aram_service.get_balanced_team(number_champions, None)
  except:
    return 'Invalid command'

def aram_default(message):
  return aram_service.get_balanced_team(15, None)

client.run(os.getenv('TOKEN'))