#!/usr/bin/env python3

import login
import time

def ofertas():
  d=login.login()
  d.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[3]/a/span').click()
  time.sleep(2)
  d.find_element_by_xpath('//*[@id="marketActions-tab"]')
  names=[]
  values=[]
  p=d.find_elements_by_class_name('nickname')
  v=d.find_elements_by_class_name('value')
  for x,y in zip(p[10:],v[10:]):
    if x.text !='' and y.text!='':
      names.append(x.text[4:])
      values.append(int(y.text[6:].replace('.','')))
  i=0
  for player in players:
    player.click()
    time.sleep(2)
    accept=d.find_element_by_xpath('/html/body/modal-container/div/div/fy-show-offers-modal/div[2]/div/div/div/button[1]')
    decline=d.find_elment_by_xpath('/html/body/modal-container/div/div/fy-show-offers-modal/div[2]/div/div/div/button[2]')
    back=d.find_element_by_xpath('/html/body/modal-container/div/div/fy-show-offers-modal/div[2]/div/div/div/button[3]')
    o=d.find_elements_by_class_name('offer-info')
    offer=int(o[1].text[:-2].replace('.',''))
    profit=offer/values[i]
    print(names[i])
    print(values[i])
    print(offer)
    print(profit)
    print('')
    correct=False
    while not correct:
      a=input('What do you wanna do? sell (y), not sell(n) and back(b) --> ')
      if a=='y':
        accept.click()
        correct=True
      if a=='n':
        decline.click()
        correct=True
      if a=='b':
        back.click()
        correct=True
    print('')
    print('')
  d.close()

if __name__=='__main__':
  ofertas()


