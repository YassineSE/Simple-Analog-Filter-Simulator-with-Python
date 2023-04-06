import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig



########First Order########

#####LOW PASS###########
def lowpass_step_1(T_0, w_0):
    num=np.array([T_0])
    den=np.array([1/w_0,1])           
    T1 = sig.lti(num,den)
    t, y = sig.step(T1)
    plt.axhline(y = T_0, color = 'purple', label = '$T_0$', linestyle="dashed")
    plt.title('Step response for a First Order Lowpass Filter')
    plt.suptitle('$T_0$ = {T_0}, $\omega_0$ = {w_0}'.format(T_0 = T_0, w_0 = w_0), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()

def lowpass_impulse_1(T_0,w_0):
    num=np.array([T_0])
    den=np.array([1/w_0,1])           
    T1 = sig.lti(num,den)
    t, y = sig.impulse(T1)
    plt.axhline(y = T_0, color = 'purple', label = '$T_0$', linestyle="dashed")
    plt.title('Impulse response for a First Order Lowpass Filter')
    plt.suptitle('$T_0$ = {T_0}, $\omega_0$ = {w_0}'.format(T_0 = T_0, w_0 = w_0), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()

######HIGH PASS##########
def highpass_step_1(T_inf,w_0):
    num=np.array([T_inf/w_0,0])
    den=np.array([1/w_0,1])           
    T1 = sig.lti(num,den)
    t, y = sig.step(T1)
    plt.axhline(y = T_inf, color = 'purple', label = '$T_\infty$', linestyle="dashed")
    plt.title('Step response for a First Order Highpass Filter')
    plt.suptitle('$T_\infty$ = {T_inf}, $\omega_0$ = {w_0}'.format(T_inf = T_inf, w_0 = w_0), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()

def highpass_impulse_1(T_inf,w_0):

    num=np.array([T_inf/w_0,0])
    den=np.array([1/w_0,1])           
    T1 = sig.lti(num,den)
    t, y = sig.impulse(T1)
    plt.axhline(y = T_inf, color = 'purple', label = '$T_\infty$', linestyle="dashed")
    plt.title('Impulse response for a First Order Highpass Filter')
    plt.suptitle('$T_\infty$ = {T_inf}, $\omega_0$ = {w_0}'.format(T_inf = T_inf, w_0 = w_0), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()




########SECOND ORDER#######

####LOW PASS####
##STEP##
def lowpass_step_2(T_0, w_0, m):
    num = np.array([0,0,T_0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)
    t, y = sig.step(T1)
    plt.axhline(y = T_0, color = 'purple', label = '$T_0$', linestyle="dashed")
    plt.title('Step response for a Second Order Lowpass Filter')
    plt.suptitle('$T_0$ = {T_0}, $\omega_0$ = {w_0}, m = {m}'.format(T_0 = T_0, w_0 = w_0, m=m), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()
##IMPULSE##
def lowpass_impulse_2(T_0, w_0, m):
    num = np.array([0,0,T_0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)
    t, y = sig.impulse(T1)
    plt.axhline(y = T_0, color = 'purple', label = '$T_0$', linestyle="dashed")
    plt.title('Impulse response for a Second Order Lowpass Filter')
    plt.suptitle('$T_0$ = {T_0}, $\omega_0$ = {w_0}, m = {m}'.format(T_0 = T_0, w_0 = w_0, m=m), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()

####HIGH PASS####
##STEP##
def highpass_step_2(T_inf, w_0, m):
    num = np.array([T_inf * (1/w_0**2),0,0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)
    t, y = sig.step(T1)
    plt.axhline(y = T_inf, color = 'purple', label = '$T_0$', linestyle="dashed")
    plt.title('Step response for a Second Order Highpass Filter')
    plt.suptitle('$T_\infty$ = {T_inf}, $\omega_0$ = {w_0}, m = {m}'.format(T_inf = T_inf, w_0 = w_0, m=m), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()
##IMPULSE##
def highpass_impulse_2(T_inf,w_0,m):
    num = np.array([T_inf * (1/w_0**2),0,0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)
    t, y = sig.impulse(T1)
    plt.axhline(y = T_inf, color = 'purple', label = '$T_0$', linestyle="dashed")
    plt.title('Impulse response for a Second Order Highpass Filter')
    plt.suptitle('$T_\infty$ = {T_inf}, $\omega_0$ = {w_0}, m = {m}'.format(T_inf = T_inf, w_0 = w_0, m=m), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()

####BAND PASS####
##STEP##
def bandpass_step_2(T_m,w_0,m):
    num = np.array([0,(2*T_m*m)/w_0,0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)
    t, y = sig.step(T1)
    plt.axhline(y = T_m, color = 'purple', label = '$T_m$', linestyle="dashed")
    plt.title('Step response for a Second Order Bandpass Filter')
    plt.suptitle('$T_m$ = {T_m}, $\omega_0$ = {w_0}, m = {m}'.format(T_m = T_m, w_0 = w_0, m=m), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()
##IMPULSE##
def bandpass_impulse_2(T_m,w_0,m):
    num = np.array([0,(2*T_m*m)/w_0,0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    
    #Create Transfer function
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)
    t, y = sig.impulse(T1)
    plt.axhline(y = T_m, color = 'purple', label = '$T_m$', linestyle="dashed")
    plt.title('Impulse response for a Second Order Bandpass Filter')
    plt.suptitle('$T_m$ = {T_m}, $\omega_0$ = {w_0}, m = {m}'.format(T_m = T_m, w_0 = w_0, m=m), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()

####NOTCH####
##STEP##
def notch_step_2(T_0,w_0,m):
    num = np.array([T_0*(1/((w_0)**2)), 0, T_0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])

    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)
    t, y = sig.step(T1)
    plt.axhline(y = T_0, color = 'purple', label = '$T_0$', linestyle="dashed")
    plt.title('Step response for a Second Order Band-Stop Filter')
    plt.suptitle('$T_0$ = {T_0}, $\omega_0$ = {w_0}, m = {m}'.format(T_0 = T_0, w_0 = w_0, m=m), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()
##IMPULSE##
#Create Transfer function
def notch_impulse_2(T_0,w_0,m):
    num = np.array([T_0*(1/((w_0)**2)), 0, T_0])
    den = np.array([1/w_0**2, 2*m/w_0, 1])
    x = sig.TransferFunction(num,den)
    T1 = sig.lti(num,den)
    t, y = sig.impulse(T1)
    plt.axhline(y = T_0, color = 'purple', label = '$T_0$', linestyle="dashed")
    plt.title('Impulse response for a Second Order Band-Stop Filter')
    plt.suptitle('$T_0$ = {T_0}, $\omega_0$ = {w_0}, m = {m}'.format(T_0 = T_0, w_0 = w_0, m=m), fontsize=14, fontweight='bold')
    plt.xlabel('Time [s]')
    plt.ylabel('Voltage [V]')
    plt.legend()
    plt.grid()
    plt.plot(t,y)
    plt.show()
