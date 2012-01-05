from sikuli.Sikuli import *
path_to_bot = getBundlePath().split("bot.sikuli")[0]

import sys
sys.path.append(path_to_bot + "model")
from List import *

class CardsList(List):
    # is list of cards wanted and cards for sale
    def __init__(self):
        super(CardsList, self).__init__()
        
    def add_card_to_have(self, cardname, amount):
        self._have[cardname] = amount