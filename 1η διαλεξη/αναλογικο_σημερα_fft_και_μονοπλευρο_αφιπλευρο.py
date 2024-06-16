import numpy as np
from numpy import pi,linspace,sin,abs,cos
import matplotlib.pyplot as plt
from scipy import fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *


A=5
f = 1000
T = 1/f
Nyquist = 2*f

Fs = 50*Nyquist
Ts = 1/Fs

number_of_signal_periodos = 3
Tmax = number_of_signal_periodos*T

t = linspace(0,Tmax,int(Tmax/Ts))
total_samples = len(t)

my_signal = A*sin(2*pi*f*t) + 3*sin(2*pi*2000*t)

plt.figure(1)
plt.plot(t,my_signal)
plt.xlabel('Xronos(seconds)->')
plt.ylabel('Platos->')
plt.title('Imitoniko Sima')
plt.grid('on') 

frequency_Range, amfipleyro_fft = fft_modules.amfipleyro_fasma(my_signal,t)

plt.figure(2)
plt.stem(frequency_Range,amfipleyro_fft)
plt.axis([-2*Nyquist , 2*Nyquist,-2,8])
plt.title('Kedrarismeno amfipleuro ')
plt.grid('on')

plt.figure(3)
Positive_Frequencies, monopleyro_fft= fft_modules.monopleyro_fasma(my_signal, t)
plt.stem(Positive_Frequencies,monopleyro_fft)
plt.axis([-2*Nyquist , 2*Nyquist,-2,8])
plt.title('Monopleuro')
plt.grid('on')





