import numpy as np
import hashlib


"""
    Kinda vanila Count Min Sketch Implementation
    Works with strings!
    
    TODO - add Conservative Updates!
"""
ROW_SIZE = 256
class CountMinSketch:
    def __init__(self, l = 4, conservative_updates = False):
        self.l = l
        self.CMS = np.zeros((l, ROW_SIZE))
        self.conservative_updates = conservative_updates
        
    def __hash__(self, x):
        return hashlib.md5(str(x).encode()).hexdigest()
        
    """
        Perfom increasing frequency of element by one
        Implements conservative updates logic
        
        Input:
            x - string
    """
    def Inc(self, x):
        step = 2
        score = self.__hash__(x)
        if (self.conservative_updates):
            # Increasing only mininal of values
            indices = []
            values = []
            for i in range(self.l):
                byte = int(score[i * 2 : i * 2 + step], 16)
                indices.append((i, byte))
                values.append(self.CMS[i, byte])
            min_value = min(values)
            for pair in indices:
                if (self.CMS[pair] == min_value):
                    self.CMS[pair] += 1
        else:
            for i in range(self.l):
                byte = int(score[i * 2 : i * 2 + step], 16)
                self.CMS[i, byte] += 1
            
       
    """
        Return  frequency of element x
        
        Input:
            x - string
    """
    def Count(self, x):
        step = 2
        score = self.__hash__(x)
        candidats = []
        for i in range(self.l):
            byte = int(score[i * 2 : i * 2 + step], 16)
            candidats.append(self.CMS[i, byte])
        return int(min(candidats))
        
        
        
