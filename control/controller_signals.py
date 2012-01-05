import sys, os
sys.path.append(os.path.abspath("../event/"))

from event import Signal

pre_main_loop = Signal()

pre_main = Signal()

main_session_cleanup = Signal()

post_main_loop = Signal()

post_main = Signal()

pre_transaction_record = Signal(provided_args=["products_bought"])

post_transaction_record = Signal(provided_args=["products_bought"])
