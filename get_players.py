#!/usr/bin/env python3

import pickle
import pprint
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
      if 'expiry' in cookie:
        del cookie['expiry']
      driver.add_cookie(cookie)

def get_players():
  # Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
  cookies_location = "/Users/Sergiflo/Programacion/fantasy/cookies.txt"
  options=Options()
  options.add_argument('user-data-dir:/Users/SergiFlo/Programacion/fantasy/chrome')
  
  
  #get to league, success
  d=webdriver.Chrome(chrome_options=options)
  load_cookies(d,cookies_location)
  #time.sleep(1)
  d.get('https://www.laligafantasymarca.com/login')
  time.sleep(2)
  c=d.find_element_by_xpath('/html/body/div[1]/div[1]/div/button')
  c.click()
  a=d.find_element_by_xpath('/html/body/fy-app/fy-layout/div/div/div/main/fy-login/div/div/div/div[1]/button/span')
  a.click()
  time.sleep(5)
  d.find_element_by_xpath('/html/body/fy-app/fy-layout/div/div/div/main/fy-home/div/div[1]/div[2]/div/div/fy-league-item/div/div[2]').click()
  time.sleep(2)
  d.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[2]/a/span').click()
  time.sleep(3)
  team = d.current_url
  players = []
  w_p = d.find_elements_by_class_name('nickname')
  for e in w_p:
    if e.text != '' :
      players.append((e.text[4:]).replace('í','i').replace('á','a').replace('é','e').replace('ó','o').replace('ú','u').replace('Í','I').replace('Á','A').replace('É',    'E').replace('Ó','O').replace('Ú','U').replace('à','a'))
  d.close()
  return players
  print(players)

def print_players():
  # Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
  cookies_location = "/Users/Sergiflo/Programacion/fantasy/cookies.txt"
  options=Options()
  options.add_argument('user-data-dir:/Users/SergiFlo/Programacion/fantasy/chrome')
  
  
  #get to league, success
  d=webdriver.Chrome(chrome_options=options)
  load_cookies(d,cookies_location)
  #time.sleep(1)
  d.get('https://www.laligafantasymarca.com/login')
  time.sleep(2)
  c=d.find_element_by_xpath('/html/body/div[1]/div[1]/div/button')
  c.click()
  a=d.find_element_by_xpath('/html/body/fy-app/fy-layout/div/div/div/main/fy-login/div/div/div/div[1]/button/span')
  a.click()
  time.sleep(5)
  d.find_element_by_xpath('/html/body/fy-app/fy-layout/div/div/div/main/fy-home/div/div[1]/div[2]/div/div/fy-league-item/div/div[2]').click()
  time.sleep(2)
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

