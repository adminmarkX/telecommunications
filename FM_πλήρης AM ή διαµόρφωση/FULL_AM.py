from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *

Ac,fc,Am,fm = 3.0 ,20000,1.0,2000

Tc = 1.0/fc
Tm = 1.0/fm
Tmax = 4*Tm

nyquist = 2*max(fc,fm)
Fs = 50*nyquist
Ts = 1/Fs

t = linspace(0,Tmax ,int(Tmax/Ts))
total_samples=len(t)

kf = 2*pi*4000 #stathera analogias

def fm_plot (Ac,fc,Am,fm,t,kf):
     
     info = Am*cos(2*pi*fm*t)
     carrier=Ac*cos(2*pi*fc*t)
     plt.figure(1)
     plt.plot(t,carrier)
     plt.plot(t,info)
     plt.title("Sima pliroforias kai feron")
     plt.xlabel('Xronos se sec')
     plt.ylabel('Platos se V')
     plt.show()
     
     m = kf*Am/(2*pi*fm)
     
     fm_signal = Ac * cos(2*pi*fc*t+m*sin(2*pi*fm*t))
     plt.figure(2)
     plt.plot(t,fm_signal)
     plt.plot(t,info)
     plt.title("Sima pliroforias kai sima FM")
     plt.xlabel('Xronos se sec')
     plt.ylabel('Platos se V')
     plt.show()
     
     fm_freq = fc+m*fm*cos(2*pi*fm*t)
     fmax = max(fm_freq)
     fmin = min(fm_freq)
     df = (fmax-fmin)/2
     
     return fm_signal , m ,df

fm_signal , m , df =fm_plot(Ac,fc,Am,fm,t,kf)


plt.figure(3)
Frequency_range , amfipleyro_fft = fft_modules.amfipleyro_fasma(fm_signal, t)
plt.subplot(2,1,1)
plt.stem(Frequency_range,amfipleyro_fft)
plt.grid('on')
plt.xlim(-fc-(m+5)*fm,fc+(m+5)*fm)


Positive_range , monopleuro_fft = fft_modules.monopleyro_fasma(fm_signal, t)
plt.subplot(2,1,2)
plt.stem(Positive_range,monopleuro_fft)
plt.grid('on')
plt.xlim(-fc-(m+5)*fm,fc+(m+5)*fm)

plt.figure(4)
#isxus simatos einai to tetragoniko tou platos tou monopleurou fasmatos tou simatos
power_of_signal = monopleuro_fft**2
plt.stem(Positive_range,power_of_signal)
plt.xlim(-fc-(m+5)*fm,fc+(m+5)*fm)


