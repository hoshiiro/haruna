from bs4 import BeautifulSoup as bs
import requests, json
from unidecode import unidecode as ud

class ship:

    def __init__(self, shipname):
        self.shipname = shipname
        #content = open('api/ship.html', 'r')
        content = requests.get(f'https://azurlane.koumakan.jp/{shipname}').content
        self.soup = bs(content, 'html.parser')
    
    def ship_name(self):

        sop = self.soup
        title = sop.find('meta', property='og:title')
        text = title['content']
        return str(text)
    
    def ship_type(self):
        sop = self.soup
        desc = sop.find('meta', property='og:description')
        text = desc['content']
        return str(text)
    
    def ship_description(self):
        suol = requests.get(f"https://azurlane.koumakan.jp/{self.shipname}/Quotes").content
        #suol = open('api/quote.html', 'r')
        sup = bs(suol, 'html.parser')

        body = sup.find('div', id='bodyContent')
        table = body.find('table')
        tbody = table.find_all('tr')

        de = tbody[1].find_all('td')
        desc = de[2].text

        ie = tbody[2].find_all('td')
        intro = ie[2].text

        return f"**{desc}** | {intro}"

    
    def ship_banner(self):

        sop = self.soup
        img = sop.find('meta', property='og:image')
        return str(img['content'])
    

    def geninfo(self):
        """Extract the general information table and turned it into dictionary"""

        sop = self.soup

        body = sop.find('div', id='bodyContent')
        table = body.find('table', id='General_information')
        tbody = table.find('tbody')
        tr = tbody.find_all('tr')
        
        del(tr[0])

        data = {}

        for item in tr:
            th = str(item.find('th').text).replace('\n', '')
            if tr.index(item) == 1:
                td = item.find('td').text.replace('\u2002', '').replace('\u2009', '').replace('\xa0', '').replace('→', ' → ')
            elif tr.index(item) == 4:
                td = item.find('td').text.replace('\u2002', '').replace('\u2009', '')
            else:
                td = ud(item.find('td').text)

            data[f'{th}'] = f"{td}".replace('\n', '')

        return dict(data)

    def stat_info(self):
        """Extract the statistics table and turned it into dict"""

        sop = self.soup
        body = sop.find('div', id='bodyContent')
        table1 = body.find('table', id='Statistics')
        tbody1 = table1.find('tbody')
        td = tbody1.find_all('div', class_='tabbertab')

        data = {}
        
        for tditem in td:

            table = tditem.find('table')
            tbody = table.find('tbody')
            tr = tbody.find_all('tr')
            
            tddata = []
            for item in tr:
                td = tditem.find_all('td')
                tddata += td
            

            td = item.find('td').text.replace('\n', '').replace('\u2009', '').replace('\u2002', '').replace('\xa0', ' ')
            stat = ['Health', 'Armor', 'Reload', 'Firepower', 'Torpedo', 'Evasion', 'Anti-air', 'Aviation', 'Oil Consumption', 'Luck', 'Accuracy', 'Speed', 'Anti-Submarine Warfare']
            
            title = tditem['title'].replace('\u2002', '')
            data[f"{title}"] = {}
                    
            for item in stat:
                if stat.index(f'{item}') == 1:
                    data[f"{title}"][f'{item}'] = str(tddata[stat.index(f'{item}')].text.replace('\n', ''))
                else:
                    data[f"{title}"][f'{item}'] = int(tddata[stat.index(f'{item}')].text.replace('\n', ''))

        return dict(data)


