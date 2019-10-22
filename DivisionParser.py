import requests
import DivisionModel
from bs4 import BeautifulSoup

class DivisionParser:

    def __init__(self, zoneUrl):
        self.zoneUrl = zoneUrl

    def getDivisionTenders (self):
        response = requests.get(self.zoneUrl)
        soup = BeautifulSoup(response.content, 'html5lib')

        table = soup.findAll('table', id='mytable')
        rows = table[0].findAll('tr')

        divisionTender = {}
        for row in rows:
            if row.text.find('Tender No.') == -1:
                cols = row.findAll('td')

                str1 = cols[0].text.strip()
                str2 = cols[1].text.strip()
                strurl = cols[2].findAll('a')[0].get('href')
                str3 = cols[2].text.strip()
                str4 = cols[3].text.strip()
                str5 = cols[4].text.strip()
                str6 = cols[5].text.strip()
                str7 = cols[6].text.strip()

                divisionModel = DivisionModel.DivisionModel(str2, str3, strurl, str4, str5, str6, str7)
                divisionTender[str3] = divisionModel

        return divisionTender
