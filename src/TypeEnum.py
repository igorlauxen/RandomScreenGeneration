from enum import Enum
import random

class TypeEnum(Enum):
    INPUT = 'INPUT'
    COMBOBOX = 'COMBOBOX'
    DATEPICKER = 'DATEPICKER'
    CHECKBOX = 'CHECKBOX'

    #@TODO improve this... there is totally a way better way to do this
    @classmethod
    def getRandom(cls):
        randomInteger = random.randint(0, 3)

        if (randomInteger == 0):
            return cls.INPUT
        elif (randomInteger == 1) :
            return cls.COMBOBOX
        elif (randomInteger == 2):
            return cls.DATEPICKER
        else:
            return cls.CHECKBOX

    @classmethod
    def has_value(cls, value):
        return any(value.value == item.value for item in cls)