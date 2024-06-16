from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *

ac = 4
fc = 12000
Tc = 1/fc

am = 2.4
fm = 4000
Tm=1/fm

m = am/ac

fmax = max(fc,fm)
print("To euros zwnis einai"+str(fmax))
T_max = max(Tc,Tm)

B=fmax
Nyquist = 2*B
Tmax = 3*T_max


Fs = 20*Nyquist
Ts = 1/Fs

Fs = 20*Nyquist
t = linspace(0,Tmax,int(T_max/Ts))

pliroforia = am * cos(2*pi*fm*t)
feron = ac*cos(2*pi*fc*t)

my_signal = (ac +am*cos(2*pi*fm*t)*cos(2*pi*fc*t))



plt.figure(1)
plt.plot(t,my_signal)
plt.grid('on')


plt.figure(2)
plt.plot(t,my_signal)
plt.grid('on')
plt.ylim(-2*fmax,2*fmax,4000)

#monopleuro fasma
Positive_range , monopleuro_fft = fft_modules.monopleyro_fasma(my_signal, t)
plt.figure(3)
plt.stem(Positive_range,monopleuro_fft)
plt.grid('on')

pliroforia = am * cos(2*pi*fm*t)
Amax = max(ac + pliroforia)
Amin =min(ac + pliroforia)

m = (Amax - Amin)/(Amax+Amin)
print("O diktis diamorfosis einai"+str(m))
