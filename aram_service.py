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

def get_balanced_team(number_champs, sort, user):
  balanced_team = random_aram(number_champs, sort)
  result = "Hi " + str(user) + '\n'
  result += '**Team One:**\n'
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
    version_response = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    api_version = version_response.json()[0]
    print(api_version)
    latest_cdn = f'https://ddragon.leagueoflegends.com/cdn/{api_version}/data/en_US/champion.json'
    response = requests.get(latest_cdn)
    champ_json = response.json()['data']
    champs = ''
    for key in champ_json.keys():
      champs += champ_json[key]['name'] + ','
    champs = champs[:-1] #remove last comma from string
    replit_db_crud.save_champs(champs)
    return True
  except:
    return False