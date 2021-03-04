from replit import db

def get_champs():
  champions = db["champs"]
  champions = champions.split(',')
  return champions

def save_champs(champs):
  db["champs"] = champs