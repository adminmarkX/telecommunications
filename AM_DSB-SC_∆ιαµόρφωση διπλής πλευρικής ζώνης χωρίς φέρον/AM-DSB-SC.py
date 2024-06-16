
from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *


fm = 1000 #sixnotita ferron
fc = 10000 #sixnotita carrier

ac = 3 #platos carrier
am = 1 #platos ferron

Tm = 1/fm #periodos ferron 
Tc = 1/fc #periodos carrier

fmax = max (fc,fm) #μεγιστη συχνοτητα σηματων
T_max = max(Tc,Tm) #μεγιστο περιοδοσ σηματων
Amax = max(ac,am) #μεγιστο πλατος σηματων

B=fmax  # ευρος ζωνης σηματων
Nyquist = 2*B #ελαχιστη συχνοτητα διγματοληψειας

Tmax = 3*T_max #thelo na zwgrafiso toso egw sto pinaka meta

# print sixnotita digmatolipsias kai periodos digmatolipsias

Fs = 100*Nyquist
print('Fs='+str(Fs))
Ts = 1/Fs
print('Ts ='+str(Ts))

t = linspace(0, Tmax , int(Tmax/Ts))

#orismos simaton pliroforias kai ferontos

pliroforia = am * cos(2*pi*fm*t)
feron = ac * cos(2*pi*fc*t)

#AM_DSB_SC ORISMOS
AM_DSB_SC = feron*pliroforia

#ORISMOS PERIBALOUSON
#PANO PERIBALOUSAS Ac+pliroforia
#KATW PERIBALOUSAS Ac-pliroforia

plt.figure(1)

#PLhroforia
plt.subplot(3,1,1)
plt.plot(t,pliroforia)
plt.title('Plhroforia')
plt.ylabel('Platos PLhroforias [V]')
plt.xlabel('Xronos[sec]')

#feron 
plt.subplot(3,1,2)
plt.plot(t,feron)
plt.title('feron')
plt.ylabel('Platos feron [V]')
plt.xlabel('Xronos[sec]')

#AM_DSB_SC GRAFIMA
plt.subplot(3,1,3)
plt.plot(t,AM_DSB_SC)
plt.plot(t,ac*pliroforia)
plt.plot(t,-ac*pliroforia)
plt.title('AM_DSB_SC')
plt.ylabel('Platos AM_DSB_SC [V]')
plt.xlabel('Xronos[sec]')

plt.show()


plt.figure(2)
Frequency_range , amfipleyro_fft = fft_modules.amfipleyro_fasma(AM_DSB_SC, t)
plt.subplot(2,1,1)
plt.stem(Frequency_range,amfipleyro_fft)
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)
plt.ylim(0,1.5*Amax)


Positive_range , monopleuro_fft = fft_modules.monopleyro_fasma(AM_DSB_SC, t)
plt.subplot(2,1,2)
plt.stem(Positive_range,monopleuro_fft)
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)
plt.ylim(0,Amax**2)

plt.figure(3)
#isxus simatos einai to tetragoniko tou platos tou monopleurou fasmatos tou simatos
power_of_signal = monopleuro_fft**2
plt.stem(Positive_range,power_of_signal)
plt.xlabel('Suxnotita (Hz)->')
plt.ylabel('Isxus->')
plt.title('Fasma isxuos AM-DSB-LC simatos')
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)
plt.ylim(0,Amax**2)


 

































 