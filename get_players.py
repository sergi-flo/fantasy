#!/usr/bin/env python3

import time
import login

def get_players():
  d=login.login()
  d.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[2]/a/span').click()
  time.sleep(3)
  team = d.current_url
  players = []
  w_p = d.find_elements_by_class_name('nickname')
  for e in w_p:
    if e.text != '' :
      players.append((e.text[4:]).replace('í','i').replace('á','a').replace('é','e').replace('ó','o').replace('ú','u').replace('Í','I').replace('Á','A').replace('É',    'E').replace('Ó','O').replace('Ú','U').replace('à','a'))
  teams=d.find_elements_by_xpath('//div[@class="lineUp col-sm-12 text-center animated fadeIn fast"]//span[@class="team-img rotate45"]')
  ts=[]
  for e in teams:
    ts.append(e.get_attribute('style'))
  d.close()
  return players, ts
  #print(players)

def print_players():
  d=login.login()
  d.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[2]/a/span').click()
  time.sleep(3)
  team = d.current_url
  players = []
  w_p = d.find_elements_by_class_name('nickname')
  for e in w_p:
    if e.text != '' :
      players.append((e.text[4:]).replace('í','i').replace('á','a').replace('é','e').replace('ó','o').replace('ú','u').replace('Í','I').replace('Á','A').replace('É',    'E').replace('Ó','O').replace('Ú','U').replace('à','a'))
  d.close()
  #return players
  print(players)

if __name__=='__main__':
 a=input('1-Return players, 2-Print players --> ')
 if a=='1':
  get_players()
 else:
  print_players()

