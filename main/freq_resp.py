import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig

def highpass_2(T_inf, w_0, m):

    #num and den of Transfer Function
    num = np.array([T_inf * (1/w_0**2),0,0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)

    #Create X axis
    f=10**np.linspace(0,6,200)
    w=2*np.pi*f
    
    #Frequency response
    w,Tjw=sig.freqresp(T1, w)
    
    #Create the asymptote
    H=np.abs(T_inf)  * np.ones(f.shape,dtype=complex) #matrice de 1
    i=np.nonzero(w<=w_0)
    H[i]= np.abs(T_inf)*(1/w_0**2) * (1j*w[i])**2

    ##Big Title##
    plt.suptitle('$T_\infty$ = {T_inf}, $\omega_0$ = {w_0}, m = {m}'.format(T_inf = T_inf, w_0 = w_0, m = m), fontsize=14, fontweight='bold')
    #######Create Magnitude Subplot#####
    plt.subplot(211)
    plt.grid(True)  

    #Draw the cutoff frequency line
    plt.axvline(x = w_0, color = 'green', label = '$\omega_0$', linestyle="dashed")
    
    #Draw T_inf
    plt.axhline(y = T_inf, color = 'purple', label = '$T_\infty$', linestyle="dashed")

    #Draw the Magnitude
    plt.loglog(w,abs(Tjw),label="Magnitude",color = "red")
    #Draw The Magnitude Asymptote
    plt.loglog(w, abs(H), label = "Asymptote", color = "blue")
    #Draw the labels and axis
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]')
    plt.ylabel('|T(j$\omega$)|');plt.title('Magnitude');plt.legend()
    

    #####Create the Phase subplot#####    
    plt.subplot(212)
    plt.grid(True)

    #Draw the Phase
    plt.semilogx(w,180/np.pi*np.angle(Tjw), color="red", label="Phase")
    #Draw the phase asymptote
    plt.semilogx(w,180/np.pi*np.angle(H),label='Asymptote', color="blue")
    #Draw the labels and axis
    plt.title("Phase")
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]');plt.ylabel('arg(T($j\omega$))');plt.legend()
    
    #Horizontal space between subplots
    plt.subplots_adjust(hspace=0.6)
    #Display all
    plt.show()




def lowpass_2(T_0, w_0, m):
    #num and den of Transfer Function
    num = np.array([0,0,T_0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)

    #Create X axis
    f=10**np.linspace(0,6,200)
    w=2*np.pi*f
    
    #Frequency response
    w,Tjw=sig.freqresp(T1, w)
    
    #Create the asymptote
    H= np.abs(T_0)* np.ones(f.shape,dtype=complex) #matrice de 1
    i=np.nonzero(w>=w_0)
    H[i]= np.abs(T_0)*(1/w_0**-2) * (1j*w[i])**-2

    ##Big Title##
    plt.suptitle('$T_0$ = {T_0}, $\omega_0$ = {w_0}, m = {m}'.format(T_0 = T_0, w_0 = w_0, m = m), fontsize=14, fontweight='bold')
    #######Create Magnitude Subplot#####
    plt.subplot(211)
    plt.grid(True)  

    #Draw the cutoff frequency line
    plt.axvline(x = w_0, color = 'green', label = '$\omega_0$', linestyle="dashed")
    
    #Draw T_inf
    plt.axhline(y = T_0, color = 'purple', label = '$T_0$', linestyle="dashed")

    #Draw the Magnitude
    plt.loglog(w,abs(Tjw),label="Magnitude",color = "red")
    #Draw The Magnitude Asymptote
    plt.loglog(w, abs(H), label = "Asymptote", color = "blue")
    #Draw the labels and axis
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]')
    plt.ylabel('|T(j$\omega$)|');plt.title('Magnitude');plt.legend()
    

    #####Create the Phase subplot#####    
    plt.subplot(212)
    plt.grid(True)

    #Draw the Phase
    plt.semilogx(w,180/np.pi*np.angle(Tjw), color="red", label="Phase")
    #Draw the phase asymptote
    plt.semilogx(w,180/np.pi*np.angle(H),label='Asymptote', color="blue")
    #Draw the labels and axis
    plt.title("Phase")
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]');plt.ylabel('arg(T($j\omega$))');plt.legend()
    
    #Horizontal space between subplots
    plt.subplots_adjust(hspace=0.6)
    #Display all
    plt.show()

def bandpass_2(T_m, w_0, m):
    #num and den of Transfer Function
    num = np.array([0,(2*T_m*m)/w_0,0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)

    #Create X axis
    f=10**np.linspace(0,6,200)
    w=2*np.pi*f
    
    #Frequency response
    w,Tjw=sig.freqresp(T1, w)
    
    #Create the asymptotes
    H=T_m  * np.ones(f.shape,dtype=complex) #matrice de 1
    i=np.nonzero(w>=w_0)
    H[i]= np.abs(T_m)*(1/w_0)**-1 * (1j*w[i])**-1
    i=np.nonzero(w<=w_0)
    H[i]= np.abs(T_m)*(1/w_0) * (1j*w[i])
    ##Big Title##
    plt.suptitle('$T_m$ = {T_m}, $\omega_0$ = {w_0}, m = {m}'.format(T_m = T_m, w_0 = w_0, m = m), fontsize=14, fontweight='bold')
    #######Create Magnitude Subplot#####
    plt.subplot(211)
    plt.grid(True)  

    #Draw the cutoff frequency line
    plt.axvline(x = w_0, color = 'green', label = '$\omega_0$', linestyle="dashed")
    
    #Draw T_inf
    plt.axhline(y = T_m, color = 'purple', label = '$T_0$', linestyle="dashed")

    #Draw the Magnitude
    plt.loglog(w,abs(Tjw),label="Magnitude",color = "red")
    #Draw The Magnitude Asymptote
    plt.loglog(w, abs(H), label = "Asymptote", color = "blue")
    #Draw the labels and axis
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]')
    plt.ylabel('|T(j$\omega$)|');plt.title('Magnitude');plt.legend()
    

    #####Create the Phase subplot#####    
    plt.subplot(212)
    plt.grid(True)

    #Draw the Phase
    plt.semilogx(w,180/np.pi*np.angle(Tjw), color="red", label="Phase")
    #Draw the phase asymptote
    plt.semilogx(w,180/np.pi*np.angle(H),label='Asymptote', color="blue")
    #Draw the labels and axis
    plt.title("Phase")
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]');plt.ylabel('arg(T($j\omega$))');plt.legend()
    
    #Horizontal space between subplots
    plt.subplots_adjust(hspace=0.6)
    #Display all
    plt.show()

#bandpass(10, 2000, 2)

def lowpass_1(T_0, w_0):
    num=np.array([T_0])
    den=np.array([1/w_0,1])           # array = tableau numpy (les opérations standard sont définies dessus ...)
    T1 = sig.lti(num,den)

    #Create X axis
    f=10**np.linspace(0,6,200)
    w=2*np.pi*f
    
    #Frequency response
    w,Tjw=sig.freqresp(T1, w)
    
    #Create the asymptote
    H=np.abs(T_0) * np.ones(w.shape,dtype=complex) #matrice de 1
	# after the cut-off frequency
    i = np.nonzero(w>=w_0)
    H[i]=np.abs(T_0) * -1j*w_0/w[i]
    

    ##Big Title##
    plt.suptitle('$T_0$ = {T_0}, $\omega_0$ = {w_0}'.format(T_0 = T_0, w_0 = w_0), fontsize=14, fontweight='bold')
    #######Create Magnitude Subplot#####
    plt.subplot(211)
    plt.grid(True)  

    #Draw the cutoff frequency line
    plt.axvline(x = w_0, color = 'green', label = '$\omega_0$', linestyle="dashed")
    
    #Draw T_inf
    plt.axhline(y = T_0, color = 'purple', label = '$T_0$', linestyle="dashed")

    #Draw the Magnitude
    plt.loglog(w,abs(Tjw),label="Magnitude",color = "red")
    #Draw The Magnitude Asymptote
    plt.loglog(w, abs(H), label = "Asymptote", color = "blue")
    #Draw the labels and axis
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]')
    plt.ylabel('|T(j$\omega$)|');plt.title('Magnitude');plt.legend()
    

    #####Create the Phase subplot#####    
    plt.subplot(212)
    plt.grid(True)

    #Draw the Phase
    plt.semilogx(w,180/np.pi*np.angle(Tjw), color="red", label="Phase")
    #Draw the phase asymptote
    plt.semilogx(w,180/np.pi*np.angle(H),label='Asymptote', color="blue")
    #Draw the labels and axis
    plt.title("Phase")
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]');plt.ylabel('arg(T($j\omega$))');plt.legend()
    
    #Horizontal space between subplots
    plt.subplots_adjust(hspace=0.6)
    #Display all
    plt.show()


def highpass_1(T_inf, w_0):
    num=np.array([T_inf/w_0,0])
    den=np.array([1/w_0,1])           # array = tableau numpy (les opérations standard sont définies dessus ...)
    T1 = sig.lti(num,den)

    #Create X axis
    f=10**np.linspace(0,6,200)
    w=2*np.pi*f

    #Frequency response
    w,Tjw=sig.freqresp(T1, w)
    
    #Create the asymptote
    H=np.abs(T_inf)  * np.ones(f.shape,dtype=complex) #matrice de 1
    i=np.nonzero(w<=w_0)
    H[i]= np.abs(T_inf)*1j*w[i]/w_0

    

    ##Big Title##
    plt.suptitle('$T_\infty$ = {T_inf}, $\omega_0$ = {w_0}'.format(T_inf = T_inf, w_0 = w_0), fontsize=14, fontweight='bold')
    #######Create Magnitude Subplot#####
    plt.subplot(211)
    plt.grid(True)  

    #Draw the cutoff frequency line
    plt.axvline(x = w_0, color = 'green', label = '$\omega_0$', linestyle="dashed")
    
    #Draw T_inf
    plt.axhline(y = T_inf, color = 'purple', label = '$T_0$', linestyle="dashed")

    #Draw the Magnitude
    plt.loglog(w,abs(Tjw),label="Magnitude",color = "red")
    #Draw The Magnitude Asymptote
    plt.loglog(w, abs(H), label = "Asymptote", color = "blue")
    #Draw the labels and axis
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]')
    plt.ylabel('|T(j$\omega$)|');plt.title('Magnitude');plt.legend()
    

    #####Create the Phase subplot#####    
    plt.subplot(212)
    plt.grid(True)

    #Draw the Phase
    plt.semilogx(w,180/np.pi*np.angle(Tjw), color="red", label="Phase")
    #Draw the phase asymptote
    plt.semilogx(w,180/np.pi*np.angle(H),label='Asymptote', color="blue")
    #Draw the labels and axis
    plt.title("Phase")
    plt.xlabel('$\omega$ [Rad.$s^{-1}$]');plt.ylabel('arg(T($j\omega$))');plt.legend()
    
    #Horizontal space between subplots
    plt.subplots_adjust(hspace=0.6)
    #Display all
    plt.show()
