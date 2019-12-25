#!/usr/bin/env python3

import players_file
import futbolfantasy

def print_prob():
  team = players_file.players_from_file()
  pre = futbolfantasy.predictions()
  for e in team:
    for player in team[e]:
      for p_player in pre[e]:
        if p_player[:-4] in player:
          print(p_player)

if __name__=='__main__':
  print_prob()
