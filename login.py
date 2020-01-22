#!/usr/bin/env python3

import pickle
import pprint
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def save_cookies(driver, location):

    pickle.dump(driver.get_cookies(), open(location, "wb"))


def load_cookies(driver, location, url=None):

    cookies = pickle.load(open(location, "rb"))
    driver.delete_all_cookies()
    # have to be on a page before you can add any cookies, any page - does not matter which
    driver.get("https://google.com" if url is None else url)
    for cookie in cookies:
      if 'expiry' in cookie:
        del cookie['expiry']
      driver.add_cookie(cookie)


def delete_cookies(driver, domains=None):

    if domains is not None:
        cookies = driver.get_cookies()
        original_len = len(cookies)
        for cookie in cookies:
            if str(cookie["domain"]) in domains:
                cookies.remove(cookie)
        if len(cookies) < original_len:  # if cookies changed, we will update them
            # deleting everything and adding the modified cookie object
            driver.delete_all_cookies()
            for cookie in cookies:
                driver.add_cookie(cookie)
    else:
        driver.delete_all_cookies()

def login():
  # Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
  cookies_location = "/Users/Sergiflo/Programacion/fantasy/cookies.txt"
  options=Options()
  options.add_argument('user-data-dir:/Users/SergiFlo/Programacion/fantasy/chrome')
  options.add_argument("--headless")
  options.add_argument('window-size=1920x1080')
  
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
  try:
    d.find_element_by_xpath('/html/body/fy-app/fy-layout/div/div/div/main/fy-home/div/div[1]/div[2]/div/div/fy-league-item/div/div[2]').click()
  except:
    d.find_element_by_xpath('/html/body/fy-app/fy-layout/div/div/div/main/fy-home/div/div[1]/div[2]/div/div[1]/fy-league-item/div/div[2]').click()
  time.sleep(2)
  print('Logged in ...')
  return d

if __name__=='__main__':
  login()
