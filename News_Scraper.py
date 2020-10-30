#!/usr/bin/env python
# coding: utf-8

# In[1]:

#SQLite DATABASE COMMANDS/FUNCTIONALITY

import sqlite3

def create_db():
    conn = sqlite3.connect('project.db')
    c=conn.cursor()
    c.execute('''CREATE TABLE news 
              (link text)''')
    
    conn.commit()
    conn.close()

def add_link(link):
    conn=sqlite3.connect('project.db')
    c=conn.cursor()
    entry=(link)
    c.execute("INSERT INTO news VALUES (?)", (entry,))    
    conn.commit()
    conn.close()
    
def drop():
    conn = sqlite3.connect('project.db')
    c = conn.cursor()
    c.execute('''DROP TABLE news''')
    conn.commit()
    conn.close()

def delete_all():
    conn=sqlite3.connect('project.db')
    c=conn.cursor()
    c.execute("DELETE FROM news")
    conn.commit()
    conn.close()
    
def select_all():
    conn=sqlite3.connect('project.db')
    c=conn.cursor()
    c.execute("SELECT * FROM news")
    links_list = c.fetchall()
    conn.close()
    return links_list

def is_scraped(link):
    links_list = select_all()
    for site_link in links_list:
        if link in site_link:
            return True
    return False
        
#create_db()
#add_link("som.com")
#drop()
#delete_all()
#print(select_all())
#print(is_scraped("som.com"))


#THE INTERCEPT


import requests
from bs4 import BeautifulSoup

url = "https://theintercept.com/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')

results = soup.find(id="root")
top_headline=results.find_all('a',class_="Homepage-HomepageTopStoriesHeroNode-link")
primary_headlines=results.find_all('a',class_="Homepage-HomepageTopStoriesPrimaryNode-container")
secondary_headlines=results.find_all('a',class_="Homepage-HomepageTopStoriesSecondaryNode-HomepageTopStoriesSecondaryPromo-container")

links_list=[]
message="The Intercept:\n\n"

for headline in top_headline:
    title=headline.find('h1',class_="elements-Heading-heading elements-Heading-dark Homepage-HomepageTopStoriesHeroNode-headingText")
    link=headline['href']
    if link not in links_list and not is_scraped(link):
        
        title_text=title.text
        title_text=title_text.replace('The Coronavirus Crisis','')
        title_text=title_text.replace('The War on Immigrants','')
        title_text=title_text.replace('Voices','')
        print(title_text)
        print("Link: "+link,end="\n\n")

        message+=title.text
        message+="\n"
        message+="Link: "
        message+=link
        message+="\n\n"
        
        add_link(link)
        links_list.append(link)
    
for headline in primary_headlines:
    title_block= headline.find('div',class_="Homepage-HomepageTopStoriesPrimaryNode-textBlock")
    title=title_block.find('h3',class_="elements-Heading-heading elements-Heading-dark Homepage-HomepageTopStoriesPrimaryNode-heading")
    link = headline['href']
    
    if link not in links_list and not is_scraped(link):
        
        title_text=title.text
        title_text=title_text.replace('The Coronavirus Crisis','')
        title_text=title_text.replace('The War on Immigrants','')
        title_text=title_text.replace('Voices','')
        print(title_text)
        print("Link: "+link,end="\n\n")

        message+=title.text
        message+="\n"
        message+="Link: "
        message+=link
        message+="\n\n"
        
        add_link(link)
        links_list.append(link)

    
for headline in secondary_headlines:
    title=headline.find('h4',class_="elements-Heading-heading elements-Heading-dark Homepage-HomepageTopStoriesSecondaryNode-HomepageTopStoriesSecondaryPromo-heading")
    link=headline['href']

    if link not in links_list and not is_scraped(link):
        
        title_text=title.text
        title_text=title_text.replace('The Coronavirus Crisis','')
        title_text=title_text.replace('The War on Immigrants','')
        title_text=title_text.replace('Voices','')
        print(title_text)
        print("Link: "+link,end="\n\n")

        message+=title.text
        message+="\n"
        message+="Link: "
        message+=link
        message+="\n\n"
        
        add_link(link)
        links_list.append(link)

#politics headlines
    
url = "https://theintercept.com/politics/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
results = soup.find(id="root")

headlines=results.find_all('a',class_="data-SpecialPromoData-container")

for article in headlines:
    title=article.find('h4',class_="elements-Heading-heading elements-Heading-dark data-SpecialPromoData-heading")
    link=article['href']
    
    if link not in links_list and not is_scraped(link):
        
        title_text=title.text
        title_text=title_text.replace('The Coronavirus Crisis','')
        title_text=title_text.replace('The War on Immigrants','')
        title_text=title_text.replace('Voices','')
        print(title_text)
        print("Link: "+link,end="\n\n")

        message+=title.text
        message+="\n"
        message+="Link: "
        message+=link
        message+="\n\n"
        
        add_link(link)
        links_list.append(link)
        
#national security headlines
    
url = "https://theintercept.com/national-security/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
results = soup.find(id="root")

headlines=results.find_all('a',class_="data-SpecialPromoData-container")

for article in headlines:
    title=article.find('h4',class_="elements-Heading-heading elements-Heading-dark data-SpecialPromoData-heading")
    link=article['href']
    
    if link not in links_list and not is_scraped(link):
        
        title_text=title.text
        title_text=title_text.replace('The Coronavirus Crisis','')
        title_text=title_text.replace('The War on Immigrants','')
        title_text=title_text.replace('Voices','')
        print(title_text)
        print("Link: "+link,end="\n\n")

        message+=title.text
        message+="\n"
        message+="Link: "
        message+=link
        message+="\n\n"
        
        add_link(link)
        links_list.append(link)
        
#world headlines
    
url = "https://theintercept.com/world/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
results = soup.find(id="root")

headlines=results.find_all('a',class_="data-SpecialPromoData-container")

for article in headlines:
    title=article.find('h4',class_="elements-Heading-heading elements-Heading-dark data-SpecialPromoData-heading")
    link=article['href']
    
    if link not in links_list and not is_scraped(link):
        title_text=title.text
        title_text=title_text.replace('The Coronavirus Crisis','')
        title_text=title_text.replace('The War on Immigrants','')
        title_text=title_text.replace('Voices','')
        print(title_text)
        print("Link: "+link,end="\n\n")

        message+=title.text
        message+="\n"
        message+="Link: "
        message+=link
        message+="\n\n"
        
        add_link(link)
        links_list.append(link)


#CEPR 


import requests
from bs4 import BeautifulSoup

url = "https://cepr.net/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
results_pre=soup.find(id="viewport")


links_list=[]

message += "\nCEPR:\n\n"

#main page
results=results_pre.find('div',class_="home-latest-article-wrap")
results=results.find('div',class_="english")
headlines = results.find_all('div',class_="latest-art-post")

for headline in headlines:
    block=headline.find('h2')
    sub_block = block.find('a')
    title = sub_block.text
    link = sub_block['href']
    
    if link not in links_list and not is_scraped(link):
        message += title
        message += "\n"
        message += "Link: "
        message += link
        message += "\n\n"

        print(title)
        print(link,end="\n\n")
        
        add_link(link)
        links_list.append(link)

    
#beat the press
results=results_pre.find('div',class_="home-blog-left-wrap-inner")
headline_main = results.find_all('div',class_="featured-blog-item-wrap")
headlines_other = results.find_all('div',class_="blog-item-wrap")

for headline in headline_main:
    block=headline.find('h3')
    sub_block = block.find('a')
    title = sub_block.text
    link = sub_block['href']
    
    if link not in links_list and not is_scraped(link):
        message += title
        message += "\n"
        message += "Link: "
        message += link
        message += "\n\n"

        print(title)
        print(link,end="\n\n")
        
        add_link(link)
        links_list.append(link)

for headline in headlines_other:
    block=headline.find('h3')
    sub_block = block.find('a')
    title = sub_block.text
    link = sub_block['href']
    
    if link not in links_list and not is_scraped(link):
        message += title
        message += "\n"
        message += "Link: "
        message += link
        message += "\n\n"

        print(title)
        print(link,end="\n\n")
        
        add_link(link)
        links_list.append(link)


#FAIR


import requests
from bs4 import BeautifulSoup

url = "https://fair.org/"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
results_pre = soup.find(id="ez-home-container-wrap")

message += "\nFAIR:\n\n"
links_list=[]

results=results_pre.find('div',class_="widget-wrap")

headlines = results.find_all('h2')

for headline in headlines:
    block = headline.find('a')
    title = block.text
    link = block['href']
    
    if link not in links_list and not is_scraped(link):
        message += title
        message += "\n"
        message += "Link: "
        message += link
        message += "\n\n"

        print(title)
        print(link,end="\n\n")
        
        add_link(link)
        links_list.append(link)


#Send emails for news links


import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date 

port=465
context=ssl.create_default_context()

sender_email="team17finalproject@gmail.com"
receiver_emails=["somjadhav787@gmail.com"]
receiver_names = ["Som"]

today = date.today()
today_str = today.strftime("%B %d, %Y")

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
    server.login(sender_email,"Abcd123!")
    for x in range(len(receiver_emails)):
        mail = MIMEMultipart("alternative")
        mail["From"] = "News Scraper"
        mail["To"] = receiver_emails[x]
        mail["Subject"] = "Daily Headlines for " + receiver_names[x] + " - " + today_str
        mail.attach(MIMEText(message,"plain"))
        receiver_email=receiver_emails[x]
        server.sendmail(sender_email,receiver_email,mail.as_string())


#NBER research papers


import requests
from bs4 import BeautifulSoup
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import date

url = "https://nber.org/new.html#latest"
page=requests.get(url)

soup=BeautifulSoup(page.content,'html.parser')
results = soup.find('ul')

message_nber = "\nThis week's NBER working papers:\n\n"

headlines = results.find_all('li',class_="multiline-li")

for headline in headlines:
    block = headline.find('a')
    title = block.text
    link = block['href']
    
    message_nber += title
    message_nber += "\n"
    message_nber += "Link: "
    message_nber += link
    message_nber += "\n\n"
    
port=465
context=ssl.create_default_context()

sender_email="team17finalproject@gmail.com"
receiver_email="somjadhav787@gmail.com"

today = date.today()
today_str = today.strftime("%B %d, %Y")


if date.today().weekday() == 0:
    with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
        server.login(sender_email,"Abcd123!")
        mail = MIMEMultipart("alternative")
        mail["From"] = "News Scraper"
        mail["To"] = receiver_email
        mail["Subject"] = "New NBER Working Papers for Week of " + today_str
        mail.attach(MIMEText(message_nber,"plain"))
        server.sendmail(sender_email,receiver_email,mail.as_string())
