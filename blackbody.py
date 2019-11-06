# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 01:29:20 2019
Blackbody radiation
@author: CHINTAN
"""
import matplotlib.pyplot as plt
import numpy as np
h=6.626176*10**-34
c=2.998*10**8
k=1.3807*10**-23
T=2.725
wc=2.898*10**-3  #Wein's displacement constant
fname='COBE_data.txt'
a=np.loadtxt(fname,skiprows=18,usecols=(0,1))
f=a[0:len(a),0]*c*100    #in Hz
cmb_flux=a[0:len(a),1]     
B_th=10**20*2*h*(f**3)/(((c**2)*(np.exp(h*f/(k*T))-1)))   #theoretical flux by blackbody in MJy/sr
fig=plt.figure()
ax=plt.subplot(111)
ax.plot(f*10**-11,B_th,'r',label='Theoretical intensity at 2.725 K')
ax.plot(f*10**-11,cmb_flux,'o',label='Experimental intensity of CMBR')
plt.title('CMBR compared with blackbody radiation at 2.725 K')
ax.set_xlabel('f(10^11 Hz)')
ax.set_ylabel('Spectral intensity(MJy/sr)')
ax.legend()
plt.show()      
m=np.argmax(cmb_flux)   #index at which maxima of flux occurs
ld_max=c/f[m]           #wavelength at which peak wavelength is obtained
print('Wavelength at which peak occurs is',ld_max)