import random
import requests
import replit_db_crud

def last_letter(word):
    return word[::-1]

def random_aram(number_champs, sort):
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
  if sort == 'lastletter':
    team_one = sorted(team_one, key=last_letter)
    team_two = sorted(team_two, key=last_letter)
  balanced_team = [team_one, team_two]
  return balanced_team

def get_balanced_team(number_champs, sort):
  balanced_team = random_aram(number_champs, sort)
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

def save_personalized_message(user,message):
  replit_db_crud.save_personalized_message(user.name,message)

def get_personalized_message(user):
  name = user.name
  print(name)
  if name == 'Confucius':
    result = 'Kevin is awesome!'
  elif name == 'Not Today':
    result = 'What do we say to the God of Death? ||Not Today||'
  elif name == 'xXMadreloaderXx':
    coin = random.randint(1, 2)
    if coin == 1:
      result = 'Hej'
    if coin == 2:
      result = "When you’re trying to explain a complex idea to someone, it’s extremely helpful to explain your new idea using terms, concepts, or ideas that the other person already understands. \n\nFor example, if you're talking to a seasoned finance professional, you can use terms like 'EBITDA' and 'valuation multiples' and they'll understand them. \n\nHowever, if you’re speaking to someone unfamiliar with finance, you’ll want to say, 'how much money a business keeps after paying all the bills,' and 'how much someone would pay to buy the company.' You want to change your choice of words to be appropriate for your audience's level of pre-existing knowledge. This is especially the case when your audience isn’t familiar with the topic at hand."
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
  elif name == 'Zenavi':
    result = 'This is fine! :fire:'
  elif name == 'Scoogie':
    result = 'WoW'
  elif 'ellie' in name:
    result = 'DJJJJJJJJ ~~Khaled~~ Beth :musical_note:'
  else:
    result = ':smiley:'
  return result