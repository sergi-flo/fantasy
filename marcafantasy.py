#!/usr/bin/env python3

import login
import time
import sys

def get_all_players():
  res={'Barcelona':[], 'Real Madrid':[], 'Sevilla':[], 'Atlético':[], 'Real Sociedad':[], 'Getafe':[], 'Athletic':[], 'Valencia':[], 'Levante':[], 'Villarreal':[], 'Granada':[], 'Osasuna':[], 'Betis':[], 'Valladolid':[], 'Alavés':[], 'Eibar':[], 'Mallorca':[], 'Celta':[], 'Leganés':[], 'Espanyol':[]}
  d=login.login()
  d.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[3]/a/span').click()
  time.sleep(2)
  d.find_element_by_xpath('//*[@id="searchPlayer-tab"]').click()
  time.sleep(5)
  p=d.find_elements_by_xpath('//div[@class="search-player"]//span[@class="name"]')
  t=d.find_elements_by_xpath('//div[@class="search-player"]//td[@class="team"]')
  tot=len(p)*len(res)
  i=0
  for x,y in zip(p,t):
    for e in res:
      percents=round(100*i/tot, 1)
      bar='#'*(int(round(60*i/float(tot))))+'-'*(60-(int(round(60*i/float(tot)))))
      sys.stdout.write('[%s] %s%s ---> %s\r'%(bar,percents,'%','Loading players'))
      sys.stdout.flush()
      if e.lower() in y.text.lower():
        res[e].append((x.text).replace('í','i').replace('á','a').replace('é','e').replace('ó','o').replace('ú','u').replace('Í','I').replace('Á','A').replace('É','E').replace('Ó','O').replace('Ú','U').replace('à','a').replace('ć','c'))
      i+=1
  d.close()
  #print(res)
  return res



if __name__=='__main__':
  get_all_players()
