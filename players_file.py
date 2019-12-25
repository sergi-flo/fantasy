#!/usr/bin/env python3

import get_players
import futbolfantasy
import marcafantasy
import json

def players_to_file():
  d={}
  pre = futbolfantasy.predictions()
  players = get_players.get_players()
  for team in pre:
    for player in players:
      for p_pre in pre[team]:
        if p_pre[:-4].lower() in player.lower(): #compare player from futbolfantasy to lalgiamarca
          if team in d:
            d[team].append(player)
          else:
            d[team]=[player]


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

if __name__=='__main__':
  a=input('1-Team player to file, 2-All players to file, 3-All marca players to file --> ')
  if a == '1':
    players_to_file()
  elif a == '3':
    all_marca_players_to_file()
  else:
    all_players_to_file()
