from core import Filter
from scipy.signal import lti
import numpy as np


class Second_Order():

    def has_overshoot(self):
        return (self.m < 1)
    
    def get_w_p(self):
        if self.has_overshoot():
            w_p = self.w_0*np.sqrt(1-(self.m**2))
        else:
            w_p = None 
        return w_p 


class LP(Second_Order, Filter):

    def __init__(self, T0, m, w_0):
        self.type = "LP"
        self.T0 = T0
        self.w_0 = w_0 
        self.m = m

    def get_sys(self):
        num = np.array([self.T0])
        den = np.array([1/(self.w_0**2), 2*self.m/self.w_0, 1])  
        return lti(num, den)
    
    def has_resonance(self):
        return  (self.m < 1/np.sqrt(2))
    
    def get_params(self):
        return {"type": self.type,
                "gain_low": self.T0, 
                "Q": 1/(2*self.m),
                "has_overshoot": self.has_overshoot(),
                "w_p": self.get_w_p()
                }


class HP(Second_Order, Filter):

    def __init__(self, Too, m, w_0):
        self.type = "HP"
        self.Too = Too 
        self.w_0 = w_0 
        self.m = m

    def get_sys(self):
        num = np.array([self.Too * (1/self.w_0**2),0,0])
        den = np.array([1/(self.w_0**2), 2*self.m/self.w_0, 1])  
        return lti(num, den)
    
    def has_resonance(self):
        return  (self.m < 1/np.sqrt(2))
    
    def get_params(self):
        return {"type": self.type,
                "gain_high": self.Too, 
                "Q": 1/(2*self.m),
                "has_overshoot": self.has_overshoot(),
                "w_p": self.get_w_p()
                }
    

