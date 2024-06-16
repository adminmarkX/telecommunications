from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *


A=5
f = 1000
T=1/f
Nyquist = 4000

Fs = 50*Nyquist

Ts = 1/Fs
number_of_signal_periods = 3
Tmax = number_of_signal_periods*T

t = linspace(0,Tmax,int(Tmax/Ts))
total_samples = len(t)

my_signal = A*sin(2*pi*2000*t)

plt.figure(1)
plt.plot(t,my_signal)
plt.xlabel('χρονος (seconds)->')
plt.xlabel('Πλατος->')
plt.xlabel('Ημμιτονικο Σημα')
plt.grid('on')


#υπολογισμος των φασματων μεσο συναρτησεων
Frequency_range , amfipleyro_fft = fft_modules.amfipleyro_fasma(my_signal, t)
plt.figure(2)
plt.stem(Frequency_range,amfipleyro_fft)
plt.axis([-5000,5000,-2,8])
plt.yticks(arange(-1,5,0.5))
plt.xticks(arange(-5000,5000,1000))
plt.title('Kentrarismeno amfipleuro fasma apo -5000 eos 5000')
plt.grid('on')

plt.figure(3)
Positive_frequencies , monopleuro_fft = fft_modules.monopleyro_fasma(my_signal, t)
plt.stem(Positive_frequencies,monopleuro_fft)
plt.axis([-5000,5000,-2,8])
plt.title('Monopleuro fasma apo -5000 eos 5000')
plt.grid('on')




