import pandas as pd
from math import log
from basstatpl.core.util.tools import approach

class BaseCalcs(object):
    def __init__(self, data = None):
        if str(type(data)) == "<class 'list'>":
            self.n = len(data)
            self.minimum = min(data)
            self.maximum = max(data)
        
        elif str(type(data)) == "<class 'dict'>":
            self.n = sum(list(data.values()))
            ftype = str(type(list(data.keys())[0]))
            
            if ftype == "<class 'tuple'>":
                self.minimum = min(data)[0]
                self.maximum = max(data)[1]
            
            elif ftype == "<class 'int'>" or ftype == "<class 'float'>":
                self.minimum = min(data)
                self.maximum = max(data)
        
        self.classes = 1 + (3.3 * log(self.n,10))
        self.rank = self.maximum - self.minimum
        self.interval = self.rank/approach(self.classes)
        self.amplitude = approach(self.interval)