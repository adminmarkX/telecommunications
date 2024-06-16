from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *

A=5
f = 1000
T = 1/f
nyquist_freq = 2*f

Fs = 50*nyquist_freq #prepei na einai toulaxiston panw apo 2*f
Ts = 1/Fs
number_of_signal_periods = 3
Tmax = number_of_signal_periods*T

t = linspace(0,Tmax,int(Tmax/Ts))

total_samples = len(t)

my_signal = A*sin(2*pi*f*t) + 3*sin(2*pi*2000*t)

# Sxediasi tou simatos
plt.figure(1)
plt.plot(t,my_signal)
plt.xlabel('Xronos (seconds) - >')  
plt.ylabel('Platos - >')
plt.title('To imitoniko sima')
plt.grid('on')


#upologismos ton fasmaton meso synartiseon

#upologismos amfipleurou fasmatos
Frequency_range , amfipleyro_fft = fft_modules.amfipleyro_fasma(my_signal, t)
plt.figure(2)
plt.stem(Frequency_range,amfipleyro_fft)
plt.axis([-5000,5000,-2,8])
plt.title('Kedrarismeno amfileuro fasma apo -5000 eos 5000')
plt.grid('on')


#upologismos ton monopleurou fasmatos
Positive_freq , monopleuro_fft = fft_modules.monopleyro_fasma(my_signal, t)
plt.figure(3)
plt.stem(Positive_freq,monopleuro_fft)
plt.axis([-5000,5000,-2,8])
plt.title('Kedrarismeno monopleuro fasma -5000 eos 5000')
plt.grid('on')

