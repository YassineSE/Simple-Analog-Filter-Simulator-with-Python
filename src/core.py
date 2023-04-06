from scipy.signal import lti
import numpy as np
import matplotlib.pyplot as plt


class Filter():
    """Main class for all the filters"""

    def __init__(self, name="filter"):
        self.name = name
    
    def get_sys(self):
        """get the scipy lti object"""
        return lti([1], [1, 1])

    def plot_bode(self, w=None):
        sys = self.get_sys()
        w, Hjw = sys.freqresp(w=w)

        # plot module
        plt.subplot(211)
        plt.grid(True)  
        plt.loglog(w,abs(Hjw), label="Magnitude")
        plt.grid(True)
        plt.xlabel('$\omega$ [Rad.$s^{-1}$]')
        plt.ylabel('|T(j$\omega$)|')
        plt.title('Magnitude')
    
        # plot phase
        plt.subplot(212)
        plt.semilogx(w,(180/np.pi)*np.angle(Hjw), color="red")
        plt.grid(True)
        plt.xlabel('$\omega$ [Rad.$s^{-1}$]')
        plt.ylabel('arg(T($j\omega$))')
        plt.title("Phase")

    def plot_step(self, T=None, E=1):
        sys = self.get_sys()
        t, s = sys.step(T=T)
        s = s*E # I exploit the linear property of lti system
        plt.plot(t, s)
        plt.grid(True)
        plt.title('Step response')
        plt.xlabel('Time [s]')
        plt.ylabel('Voltage [V]')



