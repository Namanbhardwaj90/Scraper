import ZoneParser
import ZoneModel
import DivisionParser
import json

zoneParser = ZoneParser.ZoneParser()
zonesDict = zoneParser.parseZoneTable()

zoneNew = []

for zone in zonesDict:
    if zone.url != None:
        divisionParser = DivisionParser.DivisionParser(zone.url)

        zone_new = zone
        zone_new.tenders = divisionParser.getDivisionTenders()

        zoneNew.append(zone_new)

json.dumps(zoneNew.__dict__)


