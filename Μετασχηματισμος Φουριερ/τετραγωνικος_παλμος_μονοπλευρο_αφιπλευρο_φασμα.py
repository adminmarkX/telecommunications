# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 18:52:55 2021

@author: markx
"""

from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *


t = linspace(-0.05,0.05,1000)

T=0.02
f = 1/T
ton = T/2

Ts = T/200
Fs = 1/Ts
A=1


my_signal = A*signal.square(2*pi*f*(t+T/4))




# ΤΟ ΤΕΤΡΑΓΟΝΙΚΟ ΣΗΜΑ  POLLA BEEPS
plt.figure(1)
plt.plot(t,my_signal,color="red",label="Signal Square")
plt.plot(t,my_signal)
plt.ylabel("Platos")
plt.xlabel("Xronos")
plt.ylim(-2,2)
plt.axvline(0,0,1)

# ΤΟ ΑΜΦΙΠΛΕΥΡΟ ΣΗΜΑ
Frequency_Range, amfipleyro_fft =  fft_modules.amfipleyro_fasma(my_signal, t)
plt.figure(2)
plt.stem(Frequency_Range,amfipleyro_fft)
plt.grid('on')
# ΚΑΙ ΤΟ ΜΟΝΟΠΛΕΥΡΟ ΣΗΜΑ
Positive_Frequencies, monopleyro_fft  =  fft_modules.monopleyro_fasma(my_signal,t)
plt.figure(3)
plt.stem(Positive_Frequencies, monopleyro_fft)
plt.grid('on')


# TO ΠΡΩΤΟ ΜΕΡΟΣ ΤΟΥ ΣΗΜΑΤΩΣ ΜΟΥ MONO ENA BEEP
# EDO BOROUME NA TROPOPOISOUME TO KOMMATI 
my_signal[t>T/4]=0         #my_signal[t>T/4]=0              ta arxika
my_signal[t<-T/4]=0        #my_signal[t<-T/4]=0

plt.figure(4)
plt.plot(t,my_signal,color="red",label="Signal Square")
plt.plot(t,my_signal)
plt.ylabel("Platos")
plt.xlabel("Xronos")
plt.ylim(-2,2)
plt.axvline(0,0,1)

total_samples = int(len(t))
half_samples = (total_samples/2) 
  



# ΤΟ ΑΜΦΙΠΛΕΥΡΟ ΣΗΜΑ
Frequency_Range, amfipleyro_fft =  fft_modules.amfi_fasma(my_signal,t)
plt.figure(5)
plt.stem(Frequency_Range,amfipleyro_fft)
plt.grid('on')
# ΚΑΙ ΤΟ ΜΟΝΟΠΛΕΥΡΟ ΣΗΜΑ
Positive_Frequencies, monopleyro_fft  =  fft_modules.monopleyro_fasma(my_signal,t)
plt.figure(6)
plt.stem(Positive_Frequencies, monopleyro_fft)
plt.grid('on')


# SKETO FASMA 
Frequency_Range,amfipleyro_fft = fft_modules.amfipleyro_fasma(my_signal, t) 
plt.figure(7)
plt.plot(Frequency_Range,amfipleyro_fft)
plt.axis([-500,500,-1,0.2])
plt.grid('on')
