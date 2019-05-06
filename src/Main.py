from src.RandomTransanction import RandomTransactionConfig
from src.JsonHandler import saveObjectToJson

class TransationCreate:
    def create(self):
        self.screenNumber = input("How many screens do you want to have? [Expects Integer]")
        self.fieldsMin = input("What is the minimal number of fields that you want on each screen? [Expects Integer]")
        self.fieldsMax = input("What is the maximum number of fields that you want on each screen? [Expects Integer]")

        randomTransactionConfig = RandomTransactionConfig(self.screenNumber, self.fieldsMin, self.fieldsMax)
        screens = randomTransactionConfig.createScreens()
        saveObjectToJson(screens, 'transaction.json')
        print('done :)')

if __name__ == '__main__':
    transactionCreate = TransationCreate()
    transactionCreate.create()