from numpy import pi,linspace,sin,cos,abs
import matplotlib.pyplot as plt
from scipy import signal,fftpack,arange
from scipy.fftpack import fft,fftshift
import fft_modules
from fft_modules import *

fm = 30000 #sixnotita ferron
fc = 3000 #sixnotita carrier

ac = 5 #platos carrier
am = 3 #platos ferron

Tm = 1/fm #periodos ferron 
Tc = 1/fc #periodos carrier



fmax = max (fc,fm) #μεγιστη συχνοτητα σηματων
T_max = max(Tc,Tm) #μεγιστο περιοδοσ σηματων
Amax = max(ac,am) #μεγιστο πλατος σηματων

Tmax = 3*T_max

B=fmax  # ευρος ζωνης σηματων
Nyquist = 2*B #ελαχιστη συχνοτητα διγματοληψειας

Fs = 100*Nyquist
Ts = 1/Fs

t = linspace(0, Tmax , int(Tmax/Ts))

pliroforia = am * cos(2*pi*fm*t)
feron = ac * cos(2*pi*fc*t)

AM_DSB_SC = feron*pliroforia

plt.figure(1)

#PLhroforia
plt.subplot(2,1,1)
plt.plot(t,pliroforia)
plt.title('Plhroforia')
plt.ylabel('Platos PLhroforias [V]')
plt.xlabel('Xronos[sec]')


#TO AM_DSB_SC
plt.subplot(2,1,2)
plt.plot(t,AM_DSB_SC)
plt.title('Plhroforia')
plt.ylabel('Platos AM_DSB_SC [V]')
plt.xlabel('Xronos[sec]')

Positive_range , monopleuro_fft = fft_modules.monopleyro_fasma(AM_DSB_SC, t)
plt.figure(2)
plt.stem(Positive_range,monopleuro_fft)
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)
plt.ylim(0,Amax**2)

plt.figure(3)

power_of_signal = monopleuro_fft**2
plt.stem(Positive_range,power_of_signal)
plt.xlabel('Suxnotita (Hz)->')
plt.ylabel('Isxus->')
plt.title('Fasma isxuos AM-DSB-LC simatos')
plt.grid('on')
plt.xlim(-2*fmax,2*fmax)
plt.ylim(0,Amax**2)

kanoniko = ((feron+pliroforia)/2 + (am + ac)/2) 
print("kanonikopoimeni isxis einai ="+str(kanoniko))

euros_zwnis =2*fm
print("euros zwnis ="+str(euros_zwnis))

platos = ac*am
print("platos ="+str(platos))


