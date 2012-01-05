from sikuli.Sikuli import *
path_to_bot = getBundlePath().split("bot.sikuli")[0]

import sys, copy
sys.path.append(path_to_bot + "event")

from Signal import *

pre_card_get_stock = Signal(provided_args=["cardname"])

pre_card_update_stock = Signal(provided_args=["card"])

pre_card_generate_inventory_file_info = Signal()

post_card_update_stock = Signal()

post_card_generate_inventory_file_info = Signal()

card_get_stock = Signal(provided_args=["cardname"])

card_update_stock = Signal(provided_args=["card"])

card_generate_inventory_file_info = Signal()



pre_pack_get_stock = Signal()

pre_pack_update_stock = Signal()

pre_pack_generate_inventory_file_info = Signal()

post_pack_get_stock = Signal()

post_pack_update_stock = Signal()

post_pack_generate_inventory_file_info = Signal()

pack_get_stock = Signal()

pack_update_stock = Signal()

pack_generate_inventory_file_info = Signal()