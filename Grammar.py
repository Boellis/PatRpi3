#Not currently working
from googlesearch import search
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import requests

def Synonym(synonym_page):
    #synonym_page = input('What word would you like a synonym for?: ')
    #mypage = returnUrl(synonym_page)
    html_page = urlopen(synonym_page)
    #Parse the html using beautfil soup and store in the variable 'soup'
    soup = BeautifulSoup(html_page, 'html.parser')
    #Get the price
    synonym_box = soup.find('a', attrs={'data-linkid':'nn1ov4'})
    print(synonym_box)
    #Print the price
    synonym = name_box.text.strip()
    print("Synonym: " + synonym)

def Definition(definition_page):
    #definition_page = input('What word would you like the definition for?: ')
    html_page = urlopen(definition_page)
    soup = BeautifulSoup(html_page, 'html.parser')
    definition_box = soup.find('span', attrs={'class': 'dt'})
    definition = definition_box.text.strip()
    print("Definition: " + definition)
