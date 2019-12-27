#!/usr/bin/env python3

import login
import time

def ofertas():
  d=login.login()
  d.find_element_by_xpath('//*[@id="sidebar"]/div/ul/li[3]/a/span').click()
  time.sleep(2)
  d.find_element_by_xpath('//*[@id="marketActions-tab"]').click()
  names=[]
  values=[]
  bids=[]
  p=d.find_elements_by_xpath('//div[@class="market-action"]//label[@class="nickname"]')
  v=d.find_elements_by_xpath('//div[@class="market-action"]//span[@class="value"]')
  b=d.find_elements_by_xpath('//div[@class="market-action"]//span[@class="bids"]')
  for x,y,z in zip(p,v,b):
    if x.text !='' and y.text!='' and z.text!='':
      names.append(x.text[4:])
      values.append(int(y.text[6:].replace('.','')))
      bids.append(int(z.text[:1]))
  players=d.find_elements_by_xpath('//div[@class="market-action"]//div[@class="player-info"]')
  for i in range(len(players)) :
    if bids[i]==1:
      players[i].click()
      time.sleep(1)
      d.find_element_by_xpath('//div[@class="market-action"]//button[@class="btn-fantasy red"]').click()
      time.sleep(2)
      accept=d.find_element_by_xpath('/html/body/modal-container/div/div/fy-show-offers-modal/div[2]/div/div/div/button[1]')
      decline=d.find_element_by_xpath('/html/body/modal-container/div/div/fy-show-offers-modal/div[2]/div/div/div/button[2]')
      back=d.find_element_by_xpath('/html/body/modal-container/div/div/fy-show-offers-modal/div[2]/div/div/div/button[3]')
      o=d.find_elements_by_class_name('offer-info')
      offer=int(o[1].text[:-2].replace('.',''))
      profit=round(offer/values[i],3)
      print('Name----> ',names[i])
      print('Value---> ',format(values[i],','))
      print('Offer---> ',format(offer,','))
      print('Profit--> ',profit)
      print('')
      correct=False
      while not correct:
        a=input('What do you wanna do? sell (y), not sell (n) and back(b) --> ')
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
    else:
      print('Name----> ',names[i])
      print('Value---> ',format(values[i],','))
      print('')
      print('There are no bids for this player!!')
      print('')
      print('')
    time.sleep(1)
  d.close()

if __name__=='__main__':
  ofertas()
