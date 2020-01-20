#!/usr/bin/env python3

import get_players
import futbolfantasy
import marcafantasy
import json
import remaining

def players_to_file():
  #pre = futbolfantasy.predictions()
  d={'Barcelona':[], 'Real Madrid':[], 'Sevilla':[], 'Atlético':[], 'Real Sociedad':[], 'Getafe':[], 'Athletic':[], 'Valencia':[], 'Levante':[], 'Villarreal':[], 'Granada':[], 'Osasuna':[], 'Betis':[], 'Valladolid':[], 'Alavés':[], 'Eibar':[], 'Mallorca':[], 'Celta':[], 'Leganés':[], 'Espanyol':[]}
  players,ts = get_players.get_players()
  #print(players)
  #for player,t in zip(players,ts):
  #  print(player, t)
  for team in d:
    for player,t in zip(players,ts):
      if team.lower().replace('é','e').replace(' ','-') in t:
          d[team].append(player)

  print(d)

  with open('players.json','w+') as f:
    json.dump(d,f)


def players_from_file():
  with open('players.json','r') as f:
     players=json.load(f)
  return players


def all_players_to_file():
  all_players=futbolfantasy.get_all_players()
  with open('all_players.json','w+') as f:
    json.dump(all_players,f)
  

def all_players_from_file():
  with open('all_players.json','r') as f:
     all_players=json.load(f)
  return all_players


def all_marca_players_to_file():
  all_marca_players=marcafantasy.get_all_players()
  with open('all_marca_players.json','w+') as f:
    json.dump(all_marca_players,f)
  

def all_marca_players_from_file():
  with open('all_marca_players.json','r') as f:
     all_marca_players=json.load(f)
  return all_marca_players


def playing_players_to_file():
  all_playing_players=remaining.players_playing()
  with open('playing_players.json','w+') as f:
    json.dump(all_playing_players,f)
  

def playing_players_from_file():
  with open('playing_players.json','r') as f:
     all_playing_players=json.load(f)
  return all_playing_players


if __name__=='__main__':
  a=input('1-Team player to file, 2-All players to file, 3-All marca players to file, 4-Players playing to a file --> ')
  if a == '1':
    players_to_file()
  elif a == '3':
    all_marca_players_to_file()
  elif a == '4':
    playing_players_to_file()
  else:
    all_players_to_file()
