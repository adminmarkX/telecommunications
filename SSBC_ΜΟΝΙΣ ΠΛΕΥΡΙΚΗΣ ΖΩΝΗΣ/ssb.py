from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *


Ac = 3.0
fc = 10000
Am = 1.0
fm = 1000

Tm = 1/fm
Tc = 1/fc

fmax = max(fc,fm)
T_max = max (Tc,Tm)
Amax = max(Ac,Am)

B=fmax

Nyquist = 2*B
Tmax = 3*T_max

Fs = 20*Nyquist
Ts = 1/Fs

t = linspace(0,Tmax,int(Tmax/Ts))

plirforia = Am*cos(2*pi*fm*t)
feron = Ac*cos(2*pi*fc*t)

shifted_plirforia = Am*cos(2*pi*fm*t+2*pi)
shifted_feron = Ac*cos(2*pi*fc*t+2*pi)

signal_1 = shifted_plirforia
signal_2 = shifted_feron

plt.figure(1)

Frequency_range , amfipleyro_fft = fft_modules.amfipleyro_fasma(shifted_plirforia, t)
Positive_range , monopleuro_fft = fft_modules.monopleyro_fasma(shifted_plirforia, t)

plt.subplot(3,1,1)
plt.plot(t,plirforia)
plt.grid('on')

plt.subplot(3,1,2)
plt.plot(Frequency_range,amfipleyro_fft)
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)

plt.subplot(3,1,3)
plt.plot(Positive_range,monopleuro_fft)
plt.grid('on')
plt.xlim(0,2*fmax)
plt.subplots_adjust(hspace=1)

plt.figure(2)


# feron amfipleuro fasma kai monopleuro
Frequency_range , amfipleyro_fft = fft_modules.amfipleyro_fasma(shifted_feron, t)
Positive_range , monopleuro_fft = fft_modules.monopleyro_fasma(shifted_feron, t)

plt.subplot(3,1,1)
plt.plot(t,feron)
plt.grid('on')

plt.subplot(3,1,2)
plt.plot(Frequency_range,amfipleyro_fft)
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)

plt.subplot(3,1,3)
plt.plot(Positive_range,monopleuro_fft)
plt.grid('on')
plt.xlim(0,2*fmax)
plt.subplots_adjust(hspace=1)

#Periptosi eksodos me sto a1 kai sto a2

our_signal = signal_1 + signal_2
plt.figure(3)
Frequency_range , amfipleyro_fft = fft_modules.amfipleyro_fasma(our_signal, t)
Positive_range , monopleuro_fft = fft_modules.monopleyro_fasma(our_signal, t)


plt.subplot(3,1,1)
plt.plot(t,our_signal)
plt.grid('on')


plt.subplot(3,1,2)
plt.plot(Frequency_range,amfipleyro_fft)
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)

plt.subplot(3,1,3)
plt.plot(Positive_range,monopleuro_fft)
plt.grid('on')
plt.xlim(0,2*fmax)
plt.subplots_adjust(hspace=1)
