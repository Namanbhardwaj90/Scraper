#BHUSAWAL  DIVISION-S AND T,
#BSL-N-SNT-37-2019-20,
# Comprehensive Annual Maintenance Contract on Single tender basis with OEM M/s Statcon Electronic Ind,
# Single,
# 25/10/2019 15:00,
# 3

class DivisionModel:
    def __init__(self, divisionName, tenderNumber, url, tenderTitle, tenderType, dueDate, daysLeft):
        self.divisionName = divisionName
        self.tenderNumber = tenderNumber
        self.url = url
        self.tenderTitle = tenderTitle
        self.tenderType = tenderType
        self.dueDate = dueDate
        self.daysLeft = daysLeft
