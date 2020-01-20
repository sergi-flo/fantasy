#!/usr/bin/env python3

from bs4 import BeautifulSoup
#import urllib.request
import requests
from itertools import zip_longest

def change_string(x):
  a=x.replace('\t','')
  b=a.replace('\r','')
  c=b.replace('\n','')
  d=c.replace('í','i').replace('á','a').replace('é','e')    .replace('ó','o').replace('ú','u').replace('Í','I').replace('Á','A').replace('É',        'E').replace('Ó','O').replace('Ú','U').replace('à','a')
  return d

def get_players(partidos, alineaciones, niveles):
  for e in partidos[:len(partidos)-1]:
    url_partido=requests.get(e)
    soup1=BeautifulSoup(url_partido.text, 'lxml')
    jugadores=soup1.select('.juggador')
    local=soup1.find('div', class_='nombre').string
    vis=local.find_next('div', class_='nombre').string
    j_l=soup1.find('div', class_='relative campo-wrapper liga')
    j_v=j_l.find_next('div', class_='relative campo-wrapper liga')
    n=soup1.select('.tipo')
    alineaciones[local], niveles[local], alineaciones[vis], niveles[vis]=[],[],[],[]
    for e in j_l.select('.juggador'):
      x=change_string(e.string)
      alineaciones[local].append(x)
    for e in j_v.select('.juggador'):
      x=change_string(e.string)
      alineaciones[vis].append(x)
    niveles[local].append(n[0].string)
    niveles[local].append(n[1].string)
    niveles[vis].append(n[2].string)
    niveles[vis].append(n[3].string)


def get_links(j,p):
  for e in j.contents:
    if e == '\n':
      pass
    else:
      p.append(e.get('href'))

def print_dic(x,y):
  l=[]
  v=[]
  i=0
  for e in x:
    if i%2==0:
      l.append(e)
    else:
      v.append(e)
    i+=1
  for el,ev in zip(l,v):
    print(el.ljust(40), '|'.ljust(10), ev)
    a,b=y[el][0]+' - '+y[el][1],y[ev][0]+' - '+y[ev][1]
    print(a.ljust(40),'|'.ljust(10),b)
    for jl,jv in zip_longest(x[el],x[ev]):
      if jl is None:
        print('None'.ljust(40), '|'.ljust(10), jv)
      else:   
        print(jl.ljust(40),'|'.ljust(10), jv)
    print('\n')

def predictions():
   url = 'http://www.futbolfantasy.com/laliga/calendario'
   content = requests.get(url)
   soup = BeautifulSoup(content.text, 'lxml')
   u = soup.find_all(class_='resultado')
   u_p = u[len(u)-1]
   jornada = u_p.parent.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling
   #print(jornada)
   partidos = []
   alineaciones = {}
   niveles = {}
   get_links(jornada,partidos)
   #print(partidos)
   get_players(partidos,alineaciones,niveles)
   #print_dic(alineaciones,niveles)
   #print(alineaciones)
   return alineaciones

def predictions_print():
  url = 'http://www.futbolfantasy.com/laliga/calendario'
  content = requests.get(url)
  soup = BeautifulSoup(content.text, 'lxml')
  u = soup.find_all(class_='resultado')
  u_p = u[len(u)-1]
  jornada = u_p.parent.parent.parent.next_sibling.next_sibling.next_sibling.next_sibling
  #print(jornada)
  partidos = []
  alineaciones = {}
  niveles = {}
  get_links(jornada,partidos)
  #print(partidos)
  get_players(partidos,alineaciones,niveles) 
  #print_dic(alineaciones,niveles)
  #print(alineaciones)
  print_dic(alineaciones,niveles)

def games_played():
  ty,tc,tn=[],[],[]
  url = 'http://www.futbolfantasy.com/laliga/calendario'
  content = requests.get(url)
  soup = BeautifulSoup(content.text, 'lxml')
  u = soup.find_all(class_='resultado')
  u_p = u[len(u)-1]
  jornada = u_p.parent.parent.parent
  gj=[]
  for e in jornada:
    if e!='\n':
      gj.append(e)
  for e in gj:
    if e.get('class','')==['partido','terminado']:
      a=e.find_all('img')
      for x in a:
        ty.append(x['alt'])
    if e.get('class','')==['partido']:
      a=e.find_all('img')
      for x in a:
        tn.append(x['alt'])
  #print(ty,tc,tn)
  return ty,tc,tn
  
def get_all_players():
  d={}
  url = 'http://www.futbolfantasy.com/laliga/clasificacion'
  content = requests.get(url)
  soup = BeautifulSoup(content.text, 'lxml')
  teams=soup.find_all(class_='column left nombre')
  link_teams=[]
  for e in teams:
    a=e.find('a')
    link_teams.append(a.get('href')+'/plantilla')
  for link in link_teams:
    content1 = requests.get(link)
    soup1 = BeautifulSoup(content1.text, 'lxml')
    players = soup1.find_all(class_='name')
    l_players=[]
    for player in players:
      if (player.parent.parent).get('class','')!=['cedidos','posicion']:
        l_players.append((player.text).replace('í','i').replace('á','a').replace('é','e').replace('ó','o').replace('ú','u').replace('Í','I').replace('Á','A').replace('É','E').replace('Ó','O').replace('Ú','U').replace('à','a').replace('ć','c'))
    d[soup1.find(class_='nombre').text]=l_players
  return d

if __name__== "__main__":
  a=input('1-Return dic, 2-Print dic, 3-Others --> ')
  if a == '1':
    predictions()
  elif a=='3':
    games_played()
  else:
    predictions_print() 

