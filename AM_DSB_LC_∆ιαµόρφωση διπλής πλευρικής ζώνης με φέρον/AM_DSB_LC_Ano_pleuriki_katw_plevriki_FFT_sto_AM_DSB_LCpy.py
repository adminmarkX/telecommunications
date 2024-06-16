from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *


Ac,fc,Am,fm = 3,10000,1,1000
m = Am/Ac
Tm = 1/fm
Tc = 1/fc

fmax = max(fc,fm)
T_max = max(Tc,Tm)

B=fmax
Nyquist = 2*B
Tmax = 3*T_max

Fs = 20*Nyquist
Ts = 1/Fs

Fs = 20*Nyquist
t = linspace(0,Tmax,int(T_max/Ts))

pliroforia = Am * cos(2*pi*fm*t)
feron = Ac*cos(2*pi*fc*t)



Amax = max(Ac + pliroforia)
Amin =min(Ac + pliroforia)

m = (Amax - Amin)/(Amax+Amin) #deiktis diamorfosis M

AM_DSB_LC = Ac*(1+ m*cos(2*pi*fm*t))*cos(2*pi*fc*t)

Pano_peribalousa = Ac + pliroforia
Kato_peribalousa = - Ac - pliroforia
plt.figure(1)
plt.subplot(4,1,1)
#pliroforia
plt.plot(t,pliroforia)
plt.title("Pliroforia")
plt.ylabel("Platos plhroforias [V]")
plt.xlabel("Xronos se [sec]")


#feron 
plt.subplot(4,1,2)
plt.plot(t,feron)
plt.ylabel("PLatos ferontos [V]")
plt.title("Feron")
plt.xlabel("Xronos [sec]")

#AM-DSB-LC
plt.subplot(4,1,3)
plt.plot(t,AM_DSB_LC)
plt.ylabel("Platos Diamorfomenou ferontos [V]")
plt.xlabel("Xronos [sec]")

#AM-DSB-LC kai peribaloussa
plt.subplot(4,1,4)
plt.plot(t,AM_DSB_LC)
plt.plot(t,Pano_peribalousa)
plt.plot(t,Kato_peribalousa)
plt.title("AM-DSB-LC kai peribalousses")
plt.title("Platos diamorfomenou ferontos")
plt.xlabel("Xronos [sec]")

plt.show()


my_signal = AM_DSB_LC
total_samples = int(len(t)) #sinolikos aritmos deigmaton pou tha lifthoun kata tin diarkeia toy simatos
half_samples = int(total_samples/2) 

plt.figure(2)
#XRISI TIS FFT
Frequency_range , amfipleyro_fft = fft_modules.amfipleyro_fasma(my_signal, t)
plt.subplot(2,1,1)
plt.stem(Frequency_range,amfipleyro_fft)
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)
plt.ylim(0,1.5*Amax)


Positive_range , monopleuro_fft = fft_modules.monopleyro_fasma(my_signal, t)
plt.subplot(2,1,2)
plt.stem(Positive_range,monopleuro_fft)
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)
plt.ylim(0,Amax**2)

#isxus simatos einai to tetragoniko tou platos tou monopleurou fasmatos tou simatos
power_of_signal = monopleuro_fft**2
plt.stem(Positive_range,power_of_signal)
plt.xlabel('Suxnotita (Hz)->')
plt.ylabel('Isxus->')
plt.title('Fasma isxuos AM-DSB-LC simatos')
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)
plt.ylim(0,Amax**2)









