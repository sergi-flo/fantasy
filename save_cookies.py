#!/usr/bin/env python3

import pickle
import pprint
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def save_cookies(driver, location):

    pickle.dump(driver.get_cookies(), open(location, "wb"))


user=input('Email: ')
password=input('Password: ')
# Path where you want to save/load cookies to/from aka C:\my\fav\directory\cookies.txt
cookies_location = "/Users/Sergiflo/Programacion/fantasy/cookies.pkl"
options=Options()
options.add_argument('user-data-dir:/Users/SergiFlo/Programacion/fantasy/chrome')


#Save cookies
d=webdriver.Chrome(chrome_options=options)
d.get('https://es-la.facebook.com/')
time.sleep(2)
d.find_element_by_name('email').send_keys(user)
d.find_element_by_name('pass').send_keys(password)
d.find_element_by_id('loginbutton').click()
time.sleep(5)
save_cookies(d,cookies_location)
d.quit()

