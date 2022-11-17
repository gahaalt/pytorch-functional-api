#  Copyright (c) 2022 Szymon Mikler

import logging

logging.warning("Pytorch Functional was renamed to Pytorch Symbolic!")
logging.warning("Please import pytorch_symbolic instead!")

from pytorch_symbolic import *

FunctionalModel = SymbolicModel  # for backward compatilibity

