#!/usr/bin/env python3

import login
import time


def one_or_two(i,d,names,values,bids):
  for y in range(bids[i]):
    time.sleep(2)
    players1=d.find_elements_by_xpath('//div[@class="market-action"]//div[@class="player-info"]')
    players1[i].click()
    time.sleep(1)
    d.find_element_by_xpath('//div[@class="market-action"]//button[@class="btn-fantasy red"]').click()
    time.sleep(3)
    diff_of=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]')
    ofers_from=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//span[@class="offer-info text"]')
    ofers_amount=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//span[@class="offer-info"]')
    accepts=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//button[@class="btn-fantasy big green"]')
    declines=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//button[@class="btn-fantasy big red"]')
    backs=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//button[@class="btn-fantasy big outline"]')
    print('Name----> ',names[i])
    print('')
    accept=accepts[y]
    decline=declines[y]
    back=backs[y]
    o=ofers_amount[y]
    print(o.text)
    offer=int(o.text[:-2].replace('.',''))
    profit=round(offer/values[i],3)
    print(ofers_from[y].text)
    print('Value---> ',format(values[i],','))
    print('Offer---> ',format(offer,','))
    print('Profit--> ',profit)
    print('')
    correct=False
    stop=False
    while not correct:
      a=input('What do you wanna do? sell (y), not sell (n) or next offer (b) --> ')
      if a=='y':
        accept.click()
        correct=True
        stop=True
      if a=='n':
        decline.click()
        correct=True
      if a=='b':
        back.click()
        correct=True
    if stop:
      break
    print('')

def three_or_more(i,d,names,values,bids):
  for y in range(bids[i]):
    time.sleep(2)
    players1=d.find_elements_by_xpath('//div[@class="market-action"]//div[@class="player-info"]')
    players1[i].click()
    time.sleep(1)
    d.find_element_by_xpath('//div[@class="market-action"]//button[@class="btn-fantasy red"]').click()
    time.sleep(3)
    d.execute_script('''window.open("https://some.site/", "_blank");''')
    d.switch_to_window(d.window_handles[-1])
    d.get('chrome://settings')
    d.execute_script('chrome.settingsPrivate.setDefaultZoom(0.25);')
    d.switch_to_window(d.window_handles[0])
    diff_of=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]')
    ofers_from=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//span[@class="offer-info text"]')
    ofers_amount=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//span[@class="offer-info"]')
    accepts=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//button[@class="btn-fantasy big green"]')
    declines=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//button[@class="btn-fantasy big red"]')
    backs=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//button[@class="btn-fantasy big outline"]')
    print('Name----> ',names[i])
    print('')
    accept=accepts[y]
    decline=declines[y]
    back=backs[y]
    o=ofers_amount[y]
    print(o.text)
    offer=int(o.text[:-2].replace('.',''))
    profit=round(offer/values[i],3)
    print(ofers_from[y].text)
    print('Value---> ',format(values[i],','))
    print('Offer---> ',format(offer,','))
    print('Profit--> ',profit)
    print('')
    correct=False
    stop=False
    while not correct:
      a=input('What do you wanna do? sell (y), not sell (n) or next offer (b) --> ')
      if a=='y':
        d.execute_script("arguments[0].click();", accept)
        correct=True
        stop=True
      if a=='n':
        d.execute_script("arguments[0].click();", decline)
        correct=True
      if a=='b':
        d.execute_script("arguments[0].click();", back)
        correct=True
    if stop:
      break
      i-=1
    d.switch_to_window(d.window_handles[-1])
    d.execute_script('chrome.settingsPrivate.setDefaultZoom(1);')
    d.close()
    d.switch_to_window(d.window_handles[0])
    print('')


def one_or_two_no(i,d,names,values,bids):
  for y in range(bids[i]):
    time.sleep(2)
    players1=d.find_elements_by_xpath('//div[@class="market-action"]//div[@class="player-info"]')
    players1[i].click()
    time.sleep(1)
    d.find_element_by_xpath('//div[@class="market-action"]//button[@class="btn-fantasy red"]').click()
    time.sleep(3)
    diff_of=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]')
    ofers_from=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//span[@class="offer-info text"]')
    ofers_amount=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//span[@class="offer-info"]')
    backs=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//button[@class="btn-fantasy big outline"]')
    print('Name----> ',names[i])
    print('')
    o=ofers_amount[y]
    print(o.text)
    offer=int(o.text[:-2].replace('.',''))
    profit=round(offer/values[i],3)
    print(ofers_from[y].text)
    print('Value---> ',format(values[i],','))
    print('Offer---> ',format(offer,','))
    print('Profit--> ',profit)
    backs[i].click()
    print('')

def three_or_more_no(i,d,names,values,bids):
  for y in range(bids[i]):
    time.sleep(2)
    players1=d.find_elements_by_xpath('//div[@class="market-action"]//div[@class="player-info"]')
    players1[i].click()
    time.sleep(1)
    d.find_element_by_xpath('//div[@class="market-action"]//button[@class="btn-fantasy red"]').click()
    time.sleep(3)
    d.execute_script('''window.open("https://some.site/", "_blank");''')
    d.switch_to_window(d.window_handles[-1])
    d.get('chrome://settings')
    d.execute_script('chrome.settingsPrivate.setDefaultZoom(0.25);')
    d.switch_to_window(d.window_handles[0])
    diff_of=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]')
    ofers_from=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//span[@class="offer-info text"]')
    ofers_amount=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//span[@class="offer-info"]')
    backs=d.find_elements_by_xpath('//div[@class="modal-content"]//div[@class="offer animated fadeIn fast"]//button[@class="btn-fantasy big outline"]')
    print('Name----> ',names[i])
    print('')
    o=ofers_amount[y]
    print(o.text)
    offer=int(o.text[:-2].replace('.',''))
    profit=round(offer/values[i],3)
    print(ofers_from[y].text)
    print('Value---> ',format(values[i],','))
    print('Offer---> ',format(offer,','))
    print('Profit--> ',profit)
    d.execute_script("arguments[0].click();", back[i])
    print('')
    d.switch_to_window(d.window_handles[-1])
    d.execute_script('chrome.settingsPrivate.setDefaultZoom(1);')
    d.close()
    d.switch_to_window(d.window_handles[0])

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
  corr=False
  while not corr:
    inp=input('Would you like to make actions(1) or just watch offers(2)? ')
    if inp == '1':
      for i in range(len(players)) :
        if bids[i]==1 or bids[i]==2:
          one_or_two(i,d,names,values,bids)
        elif bids[i]==0:
          print('Name----> ',names[i])
          print('Value---> ',format(values[i],','))
          print('')
          print('There are no bids for this player!!') 
        else:
          three_or_more(i,d,names,values,bids)
        print('')
        print('')
        time.sleep(2)
      corr=True
    if inp == '2':
      for i in range(len(players)) :
        if bids[i]==1 or bids[i]==2:
          one_or_two_no(i,d,names,values,bids)
        elif bids[i]==0:
          print('Name----> ',names[i])
          print('Value---> ',format(values[i],','))
          print('')
          print('There are no bids for this player!!') 
        else:
          three_or_more_no(i,d,names,values,bids)
        print('')
        print('')
        time.sleep(2)
      corr=True
  d.close()


if __name__=='__main__':
  ofertas()
