class ZoneModel:
    def __init__(self, zoneName, tenderCount, url):
        self.zoneName = zoneName
        self.tenderCount = tenderCount
        self.url = url
        self.tenders = {}
