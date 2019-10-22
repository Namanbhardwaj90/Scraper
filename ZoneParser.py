import requests,html5lib
import ZoneModel

class ZoneParser:
    ZONEURL = "https://www.ireps.gov.in/epsn/home/showTenderDetails.do?listType=nitLiveSignTele"

    def __int__(self):
        pass

    def parseZoneTable (self):

        response = requests.get(self.ZONEURL)

        fullHtml = str(response.content)
        tableIndex = fullHtml.index('<td class="formLabel">Action</td>')
        tableText = fullHtml[tableIndex + len('<td class="formLabel">Action</td>'):]
        tableText = tableText.replace(r'\t', '')

        tdTrLines = tableText.split(r'\r\n')

        # RESET MACHINE TO INTITIAL STATE --->
        # EXPECTING <TR> and then <td class="formLabel" align="Left" > to start the engine
        line = 0
        entered = 0
        zones = []

        zone = None
        tenderCount = None
        url = None

        while 1:
            if line == len(tdTrLines):
                break

            if entered == 1:
                string = ''
                # Expect serial number
                thisLine = tdTrLines[line]
                serial = thisLine[len('<td class="formLabel" align="Left" >'):len(thisLine) - 5]
                line = line + 1
                entered = 2
                string = serial  # ignored
                continue

            elif entered == 2:
                thisLine = tdTrLines[line]
                zone = thisLine[len('<td class="formLabel" align="Left">'):len(thisLine) - 5]
                line = line + 1
                entered = 3
                continue

            elif entered == 3:
                thisLine = tdTrLines[line]
                tenderCount = thisLine[len('<td class="formLabel" align="Left" >'):len(thisLine) - 5]
                line = line + 1
                entered = 4
                continue

            elif entered == 4:
                thisLine = tdTrLines[line]
                if thisLine.find('href') != -1 and thisLine.find('><img src=') != -1:
                    url = thisLine[thisLine.find('href=') + len('href='):thisLine.find('><img src=')]
                line = line + 1
                entered = 0

                z = ZoneModel.ZoneModel(zone, tenderCount, url)
                zones.append(z)

                continue

            if tdTrLines[line] == '<tr>':
                if tdTrLines[line + 1].startswith('<td class="formLabel" align="Left" >'):
                    entered = 1
                    line = line + 1
                else:
                    line = line + 1
            else:
                line = line + 1

        return zones
