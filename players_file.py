#!/usr/bin/env python3

import get_players
import predictions
import json

def players_to_file():
  d={}
  pre = predictions.predictions()
  players = get_players.get_players()
  for team in pre:
    for player in players:
      for p_pre in pre[team]:
        if p_pre[:-4] in player:
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

if __name__=='__main__':
  players_to_file()

