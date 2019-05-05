import random
from src.Field import Field

class Screen:
    def __init__(self, id, nMinFieldsScreen, nMaxFieldsScreen):
        self.id = id
        self.nMinFieldsScreen = nMinFieldsScreen
        self.nMaxFieldsScreen = nMaxFieldsScreen
        self.fields = []
        self.createFields()

    def createFields(self):
        numberOfFields = random.randint(self.nMinFieldsScreen, self.nMaxFieldsScreen)
        for x in range(numberOfFields):
            field = Field(str(x) + 'screen' + str(self.id))
            self.fields.append(field)

    def getFields(self):
        return self.fields

    def getFieldsLength(self):
        return len(self.fields)