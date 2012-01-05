import sys, os

sys.path.append(os.path.realpath(__file__))

from domain import *
from control import *
from registry import *

x = Controller()

x.main()