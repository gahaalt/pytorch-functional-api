#  Copyright (c) 2022 Szymon Mikler

import logging

logging.warning("Pytorch Functional was renamed to Pytorch Symbolic!")
logging.warning("Please import pytorch_symbolic instead!")

from pytorch_symbolic import (
    Input,
    SymbolicModel as FunctionalModel,
    add_to_model,
    useful_layers,
    graph_algorithms,
    config,
)
