import discord
import os
import aram_service
import never_sleep

#Flask Server to keep repl.it alive
never_sleep.awake('https://aram-discord-bot.kloklee88.repl.co', False)

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  activity = discord.Game(name="!aram help")
  await client.change_presence(activity=activity)
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
      return

  #Process message commands
  command = message.content.strip().split(' ')
  if message.content.startswith('!aram'):
    print(command)
    if len(command) == 2:
      aram_command = command[1]
      if aram_command.startswith('<@!'):
        await message.channel.send('You must be looking for Quack bot, use !quack instead')
      elif aram_command == 'about':
        await message.channel.send(about())
      elif aram_command == 'help':
        await message.channel.send(help())
      elif aram_command == 'all':
        await message.channel.send(all())
      elif aram_command == 'total':
        await message.channel.send(total())
      elif aram_command == 'update':
        await message.channel.send('Running update... please wait...')
        await message.channel.send(update())
      elif aram_command == 'lastletter':
        await message.channel.send(last_letter(), message.author)
      else:
        await message.channel.send(aram_number(aram_command, message.author))
    else:
      await message.channel.send(aram_default(message.author))

def about():
  return 'Randomly selects champions split into 2 teams for ARAM inhouses to simulate re-rolls. Please thank my creator, Kevin :)'

def help():
  return 'Commands:\n**!aram** -- will default to 15 champions for each team\n**!aram #** -- where # is the number of champions per team, up to a max of 30\n**!aram total** -- show total number of all currently available champions used by the bot\n**!aram all** -- show all currently available champions\n**!aram update** -- get latest champions from Riot (use when list is out of date)\n**!aram about** -- bot description\n'

def all():
  return ', '.join(aram_service.get_all_champions())

def total():
  return len(aram_service.get_all_champions())

def update():
  result = aram_service.update_champions()
  if result == True:
    return 'Champions updated!'
  else:
    return 'Error. Champions were not updated.'

def last_letter(user):
  return aram_service.get_balanced_team(int(15), 'lastletter', user)

def aram_number(aram_command, user):
  try:
    number_champions = int(aram_command)
    return aram_service.get_balanced_team(number_champions, None, user)
  except:
    return 'Invalid command'

def aram_default(user):
  return aram_service.get_balanced_team(15, None, user)

client.run('')