import pandas as pd 
import numpy as np 
from abc import ABC, abstractmethod
from typing import List, Any
from typing import Optional
from smartext.processing import ProcessorMain





class SimpleProcessor(ProcessorMain):
    def __init__(self,) -> None:
        super().__init__()
        self.documents = documents


    def create_vocab(self,documents:List,char_to_split:str=' ',return_pd:bool=True) -> None:

        self.vocab = {}

        # loop documents
        for doc in documents:

            for word in self.split_simple(doc,char_to_split):

                try:
                    vocab[word] += 1
                except:
                    vocab[word] = 1
        
        if return_pd:
            df_vocab = pd.DataFrame({
                'word': list(vocab.keys()),
                'freq': list(vocab.values())
            }
            ).sort_values(by=['freq'],ascending=False)

            self.vocab = df_vocab

        return self.vocab


    def split_simple(self,doc:str,char_to_split:str=' ') -> List:

        return doc.split(char_to_split)






