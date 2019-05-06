import random
import string

from src.TypeEnum import TypeEnum

def generateRandomName(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def isMandatory():
    randomInteger = random.randint(0, 10)
    return randomInteger > 5

def getType():
    return TypeEnum.getRandom()

class Field:
    def __init__(self, id):
        if id == 0:
            raise AttributeError('ID must not be zero')
        self.type = getType()
        self.mandatory = isMandatory()
        self.name = generateRandomName()
        self.id = id

    def serialize(self):
        return self.__dict__



