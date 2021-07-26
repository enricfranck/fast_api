import requests as _request
import bs4 as _bs4
from typing import List
import json

''' Methode pour récuperer le nom de la l'application '''
def getNom(url:str)->str:
    try:
        reponse=_request.get(url);
        soup=_bs4.BeautifulSoup(reponse.text,"html.parser");
        nom=soup.find(class_="header-desktop__AppName-xc5gow-5 fzCqyh")
        return nom.get_text();
    except:
        return "erreur";
    
    
''' Methode pour récuperer le nombre de téléchargement de l'application'''
def getNbrTelecharge(url:str)->str:
    try:
        reponse=_request.get(url);
        soup=_bs4.BeautifulSoup(reponse.text,"html.parser");
        nbre=soup.find_all("span",class_='mini-stats__Info-sc-188veh1-6 hwoUxO')[0]               
        return nbre.get_text();
    except:
        return "erreur";
    

''' Methode pour récuperer la déscription de l'application'''
def getDescription(url:str)->str:
    try:
        reponse=_request.get(url);
        soup=_bs4.BeautifulSoup(reponse.text,"html.parser");
        desc=soup.find(class_="description__DescBody-sc-45j1b1-0 gdwZQU")
        return desc.get_text();
    except:
        return "erreur";
    

''' Methode pour récuperer la date de publication de l'application'''
def getDatePublication(url:str)->str:
        reponse=_request.get(url);
        soup=_bs4.BeautifulSoup(reponse.text,"html.parser");
        desc=soup.find_all('div',{"class":"mini-versions__VersionDate-sc-19sko2j-6 jeuKzx"})[0]
        return desc.get_text();
   
    

''' Methode pour récuperer la version de l'application'''
def getVersion(url:str)->str:
    try:
        reponse=_request.get(url);
        soup=_bs4.BeautifulSoup(reponse.text,"html.parser");
        vers=soup.find_all("span",class_='mini-stats__Info-sc-188veh1-6 hwoUxO')[2]    
        return vers.get_text();
    except:
        return "erreur";
