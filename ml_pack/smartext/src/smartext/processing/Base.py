import pandas as pd 
import numpy as np 
from abc import ABC, abstractmethod
from typing import List, Any
from typing import Optional



class ProcessorMain(ABC):

    def __init__(self,
    documents:List[] = [],

    ) - None:
        super().__init__()
        self.documents = documents

    def process(self):
        pass