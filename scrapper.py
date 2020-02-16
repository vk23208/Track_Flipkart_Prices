# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 08:40:51 2020

@author: Vishal Rana
"""

#youtube url
'https://www.youtube.com/watch?v=Bg9r_yLk7VY'

import requests
from bs4 import BeautifulSoup
import smtplib

#for 8GB version
url1 = 'https://www.flipkart.com/realme-x2-pro-neptune-blue-128-gb/p/itma3203d88190a3?pid=MOBFM2WZNK2HHZCM&lid=LSTMOBFM2WZNK2HHZCMBBWTEO&marketplace=FLIPKART&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=7154358a-5a23-4084-ac57-27ec3c3fdad0.MOBFM2WZNK2HHZCM.SEARCH&ppt=sp&ppn=sp&ssid=176gzseyn40000001581822840348&qH=5fb8821185bcc702'

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36"}

#for 6GB version
url2 = 'https://www.flipkart.com/realme-x2-pro-lunar-white-64-gb/p/itma3203d88190a3?pid=MOBFM2WZVWUNZGTX&lid=LSTMOBFM2WZVWUNZGTXUXZQFO&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=ram&otracker=search'    


def check_price():

    page = requests.get(url1, headers = headers)    
    soup = BeautifulSoup(page.content, 'html.parser')    
    title_8GB = soup.find(attrs = {'class':'_35KyD6'}).get_text().strip()
    price_8GB = soup.find(attrs= {'class' : '_1vC4OE _3qQ9m1'}).get_text().replace(',','')
    convertedprice1 = int(price_8GB[1:7])  
    
    page = requests.get(url2, headers = headers)    
    soup = BeautifulSoup(page.content, 'html.parser')  
    title_6GB = soup.find(attrs = {'class':'_35KyD6'}).get_text().strip()
    price_6GB = soup.find(attrs= {'class' : '_1vC4OE _3qQ9m1'}).get_text().replace(',','')
    convertedprice2 = int(price_6GB[1:7])
    
    if(convertedprice1 < 29999):
        send_mail1()
        
    if(convertedprice2 < 37999):
        send_mail2()
        
def send_mail1():
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('vk23208@gmail.com' , 'xgbvqmuognavfvsg')
    
    subject = 'Price fell down RealmeX2Pro 8GB'
    body = '''Check flipkart link   https://www.flipkart.com/realme-x2-pro-neptune-blue-128-gb/p/itma3203d88190a3?pid=MOBFM2WZNK2HHZCM&lid=LSTMOBFM2WZNK2HHZCMBBWTEO&marketplace=FLIPKART&srno=s_1_3&otracker=search&otracker1=search&fm=SEARCH&iid=7154358a-5a23-4084-ac57-27ec3c3fdad0.MOBFM2WZNK2HHZCM.SEARCH&ppt=sp&ppn=sp&ssid=176gzseyn40000001581822840348&qH=5fb8821185bcc702'''
    msg = f"Subject : {subject}\n\n{body}"
    
    server.sendmail('vk23208@gmail.com','vk23208@gmail.com',msg)
    print('Hey, Email has been sent for RealmeX2pro 8GB!')
    server.quit()
    
def send_mail2():
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('vk23208@gmail.com' , 'xgbvqmuognavfvsg')
    
    subject = 'Price fell down RealmeX2Pro 6GB'
    body = '''https://www.flipkart.com/realme-x2-pro-lunar-white-64-gb/p/itma3203d88190a3?pid=MOBFM2WZVWUNZGTX&lid=LSTMOBFM2WZVWUNZGTXUXZQFO&marketplace=FLIPKART&sattr[]=color&sattr[]=storage&sattr[]=ram&st=ram&otracker=search'''
    msg = f'Subject : {subject}\n\n{body}'
    
    server.sendmail('vk23208@gmail.com','vk23208@gmail.com',msg)
    print('Hey, Email has been sent for RealmeX2pro 6GB!')
    server.quit()
    
check_price()

