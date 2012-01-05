import sys, os
sys.path.append(os.path.abspath("../event/"))

from event import Signal

pre_buy_mode = Signal()

pre_sell_mode = Signal()
