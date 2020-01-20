#!/usr/bin/env python3
import login
import players_file
import futbolfantasy
import time, os

def players_playing():
  d=login.login()
  d.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[1]/a').click()
  time.sleep(2)
  #print(players)
  #print(len(players))
  res={}
  for i in range(12):
    p={'Barcelona':[], 'Real Madrid':[], 'Sevilla':[], 'Atlético':[], 'Real Sociedad':[], 'Getafe':[], 'Athletic':[], 'Valencia':[], 'Levante':[], 'Villarreal':[], 'Granada':[], 'Osasuna':[], 'Betis':[], 'Valladolid':[], 'Alavés':[], 'Eibar':[], 'Mallorca':[], 'Celta':[], 'Leganés':[], 'Espanyol':[]}
    players=d.find_elements_by_xpath('//div[@class="card border-light"]//h5[@class="name"]')
  #  for e in players:
  #    print(e.text)
    name=players[i].text
  #  print(name)
    players[i].click()
    if name == 'sersik9':
      d.find_element_by_xpath('//*[@id="points-tab"]').click()
    time.sleep(2)
    found=False
    while not found:
      j=d.find_elements_by_class_name('card-title')
      ts=d.find_elements_by_xpath('//div[@class="lineUp col-sm-12 text-center animated fadeIn fast"]//span[@class="team-img rotate45"]')
      if name == 'sersik9':
        l=0
        for pp in j:
          if pp.text!='':
            l+=1
        j,ts=j[:l], ts[:l]
      if name =='DaniPXX':
        break
      if len(j)==11 and len(ts)==11:
        found=True
    jp=[]
    for e in j:
      if e !='':
        jp.append((e.text).replace('í','i').replace('á','a').replace('é','e').replace('ó','o').replace('ú','u').replace('Í','I').replace('Á','A').replace('É','E').replace('Ó','O').replace('Ú','U').replace('à','a').replace('ć','c'))
    for e in p:
      for player,t in zip(jp,ts):
        if e[-5:].lower().replace('é','e') in t.get_attribute('style'):
          p[e].append(player)
    res[name]=p
    d.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[1]/a').click()
    time.sleep(1)
  #for e in res:
  #print(res)
  d.close()
  return res

def players_remaining(pp):
  res={}
  ty,tc,tn=futbolfantasy.games_played()
  if pp==None:
    return 'No playing players selected'
  plantillas=players_file.all_marca_players_from_file()
  for player in pp: #every player playing in the league
    y,c,n=0,0,0
    for team in ty: #teams that have already played
      for e in pp[player]: #e is dic of teams and players from player
        if e==team: #if team has played
          for p in pp[player][e]: #p is every player(real) of team of player that has played
            for a in plantillas[team]: #a is all players in team
              #print(p.lower(),' | ',a.lower())
              if p.lower() in a.lower():
                y+=1
                break
    res[player]=[y,11-y]
  #print(res)
  return res

def print_players_remaining():
  dr=login.login()
  dr.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[1]/a').click()
  players=dr.find_elements_by_xpath('//div[@class="card border-light"]//h5[@class="name"]')
  points=dr.find_elements_by_xpath('//div[@class="card border-light"]//span[@class="positive"]')
  clas=[]
  for x,y in zip(players,points):
    clas.append([x.text,y.text])
  dr.close()
  print('Actual date is: '.ljust(40), time.ctime())
  print('File last modification is: '.ljust(40),time.ctime(os.path.getmtime('playing_players.json')))
  print('')
  inp=input('Quieres cargar nuevas alineaciones y usarlas(1) o usar las que ya estan(2)? ')
  corr=False
  while not corr:
    if inp == '1':
      players_file.playing_players_to_file()
      pp=players_file.playing_players_from_file()
      corr=True
    elif inp == '2':
      pp=players_file.playing_players_from_file()
      corr=True
  d=players_remaining(pp)
  print('-'*53)
  print('Players'.ljust(20),'| Remaining'.ljust(8),'| Played |',' Puntos |')
  print('-'*53)
  for player in clas:
    print(player[0].ljust(20),'|    ',str(d[player[0]][1]).ljust(5),'|  ',str(d[player[0]][0]).ljust(4),'|   ',player[1].ljust(4),'|')

if __name__=='__main__':
  a=input('1-Players remaining, 2- Players playing, 3-Print players remaining ---> ')
  if a=='1':
    players_remaining()
  elif a=='3':
    print_players_remaining()
  else:
    players_playing()
