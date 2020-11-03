#!/usr/bin/env python
# coding: utf-8

# In[6]:


from bs4 import BeautifulSoup
import pandas as pd
import requests


# In[26]:


class Alernance:
    def __init__(self,total_jobs):
        self.total_offers = int(total_jobs/100)


    def Getting_Job_offers_Links(self):
        Links = []
        Name = []
        print(self.total_offers)
        for item in range(self.total_offers):
            leng = item*100
            try:
                r= requests.get('https://www.alternance.fr/api/offer/list?from='+str(leng)+'&size=100')
                for i in range(len(r.json()['data'])):
                    try:
                        Links.append("https://www.alternance.fr/offres/"+str(r.json()['data'][i]['slug'])+"-"+str(r.json()['data'][i]['id'])+".html")
                        Name.append(r.json()['data'][i]['company']['name'])
                        print("https://www.alternance.fr/offres/"+str(r.json()['data'][i]['slug'])+"-"+str(r.json()['data'][i]['id'])+".html")
                    except:
                        pass
                print("============================================================="+str(len(Links))+"===========================================================")

            except:
                pass

        links_data = {'Company Name':Name,'Links':Links}
        return links_data
    
    
    def Getting_Data_from_Offer_Links(self,Links,companies):

        r = requests.get(Links)
        soup = BeautifulSoup(r.text, 'html.parser')

        title = ''
        publish = ''
        category = ''
        sect = ''
        type_cont = ''
        dure = ''
        date = ''
        ville =''
        degree = ''
        comp = companies


        try:
            title = soup.find('h1').text
            print(soup.find('h1').text)
        except:
            pass

        try:
            publish = soup.find('p',{'class':'author'}).text.strip().split('\n')[0]
        except:
            pass

        try:
            category = soup.find('div',{'class':'domain-link'}).text
        except:
            pass


        try:
            for i in soup.findAll('div',{'class':'offer-info'}):
                if 'Secteurs' in i.text.strip().replace('\n',' : '):
                    sect = i.text.strip().replace('\n',' : ').replace('Secteurs','').strip()
                elif 'Type de contrat' in i.text.strip().replace('\n',' : '):
                    type_cont = i.text.strip().replace('\n','').replace('Type de contrat','').strip()
                elif 'Date de début de la mission' in i.text.strip().replace('\n',' : '):
                    date = i.text.strip().replace('\n','').replace('Date de début de la mission','').strip()
                elif 'Durée de la mission' in i.text.strip().replace('\n',' : '):
                    dure = i.text.strip().replace('\n','').replace('Durée de la mission','').strip()
                elif 'Ville' in i.text.strip().replace('\n',' : '):
                    ville = i.text.strip().replace('\n','').replace('Ville:','').strip()
                elif "Niveaux d'études" in i.text.strip().replace('\n',''):
                    degree = i.text.strip().replace('\n','').replace("Niveaux d'études",'').strip()
        except:
            pass

        offers_data = {'Title':title,'Company Name':comp,'Publish Date':publish,'Category':category,'Secteurs':sect,'Type de contrat':type_cont,'Date de début de la mission':date,'Duree':dure,'Ville':ville,'Degree':degree}
        return offers_data
        
        
        


        


        

