#!/usr/bin/env python3

import futbolfantasy, get_players, login, marcafantasy, ofertas, players_file, remaining, save_cookies, team_prob

def menu():
  end=False
  while(end!=True):
    print('------------------------------------------------------')
    print('Menu:\n1-Save cookies\n2-Probability of all line-up\n3-Probability of playing your players\n4-Get all players from marca into txt\n5-Get all you players into txt\n6-Ofers from market\n7-Remaining players to play\n8-Exit')
    num=input('What do you wanna do --> ')
    print('------------------------------------------------------')
    if num=='1':
      save_cookies.saveCookies()
    if num=='2':
      futbolfantasy.predictions_print()
    if num=='3':
      team_prob.print_prob()
    if num=='4':
      players_file.all_marca_players_to_file()
    if num=='5':
      players_file.players_to_file()
    if num=='6':
      ofertas.ofertas()
    if num=='7':
      remaining.print_players_remaining()
    if num=='8':
      print('\nGoodbye!! :D')
      end=True

if __name__=='__main__':
  menu()
