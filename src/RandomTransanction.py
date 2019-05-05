import random

from src.Screen import Screen

class RandomTransactionConfig:

    def __init__(self, nScreens, nMinFieldsScreen, nMaxFieldsScreen):
        self.nScreens = nScreens
        self.nMinFieldsScreen = nMinFieldsScreen
        self.nMaxFieldsScreen = nMaxFieldsScreen
        self.screens = []

    def __init__(self):
        self.nScreens = 2
        self.nMinFieldsScreen = 1
        self.nMaxFieldsScreen = 7
        self.screens = []

    def createScreens(self):
        for x in range (self.nScreens):
            self.screens.append(Screen(x))