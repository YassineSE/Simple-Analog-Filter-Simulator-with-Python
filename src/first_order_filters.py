from core import Filter
from scipy.signal import lti
import numpy as np


class LP(Filter):

    def __init__(self, T0, w_0):
        self.type = "LP"
        self.T0 = T0 
        self.w_0 = w_0 

    def get_sys(self):
        num = np.array([self.T0])
        den = np.array([1/self.w_0,1])  
        return lti(num, den)
    
    def get_params(self):
        return {"type": self.type,
                "gain_low": self.T0, 
                "tau": 1/self.w_0}

   
class HP(Filter):

    def __init__(self, Too, w_0):
        self.type = "HP"
        self.Too = Too 
        self.w_0 = w_0 

    def get_sys(self):
        num = np.array([self.Too, 0])
        den = np.array([1/self.w_0, 1])  
        return lti(num, den)
    
    def get_params(self):
        return {"type": self.type,
                "gain_high": self.Too, 
                "tau": 1/self.w_0}
    
