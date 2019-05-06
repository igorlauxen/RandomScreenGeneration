import random

from src.Screen import Screen

class RandomTransactionConfig:

    def __init__(self, nScreens, nMinFieldsScreen, nMaxFieldsScreen):
        self.nScreens = nScreens
        self.nMinFieldsScreen = nMinFieldsScreen
        self.nMaxFieldsScreen = nMaxFieldsScreen
        self.screens = []

    def createScreens(self):
        times = self.returnHowManyScreen()
        for x in range(times):
            newScreen = Screen(x, int(self.nMinFieldsScreen), int(self.nMaxFieldsScreen))
            self.screens.append(newScreen)
        return self.screens

    def returnHowManyScreen(self):
        times = 0
        if isinstance(self.nScreens, str):
            times = int(self.nScreens)
        else:
            times = self.nScreens
        return times