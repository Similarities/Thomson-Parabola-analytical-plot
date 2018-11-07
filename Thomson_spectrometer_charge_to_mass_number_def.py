
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 01 11:56:10 2015

@author: Zombie.Soc//similarities
"""


import matplotlib.pyplot as plt
import matplotlib.image as mpimg




print ("Reconstruction of Thomson spectrometer parabolas - to check parameters")



#Parameters
# !!! 0 point coordinates in px
x0 = 825
y0 = 305
B = 0.21 #magnetic field strength in Tesla
D = 0.670 # Drift of spectrometer
q = 1.6027E-19 # elemental charge q
l = 0.05 # lenght of magnet in m
Abbildung = 0.00004521 # magnification factor m/pix
mp = 1.673E-27 # mass proton
E1 = 3.985E3 # Potential of Efield in applied Voltage
Le = 0.0098 # distance of field plates in m
EF = E1/Le
v0 = 1E7 #v0 in m/s

print("charge to mass ratio?")
ZA= input("Z/A:" ) # charge to mass number of ion


# 0.355 +/- 0.002 trace1 between C4+ und  O5+
# 0.344 +/- 0.002 trace2 between C4+ und O5+
# 0.466 +/- 0.005 trace between C6+ und O7+
#0.428 +/- 0.     trace after O7+
#0.405 +/-0.002 trace after C+5
#0.32  +/- 0.005 trace after C4+
#0.28  +/-0.005   trace after O5+







def xp(x1): 
    
    xp = [x1]
    
    for i in range (1, x1):
       
       xp.append(x1 - i)

    return xp

         
         
         
def parabely(x1,ZA):
    
    hh = [y0]
    
    const = (mp * EF / (ZA *q * l * D * B ** 2))
    
    for i in range (1, x1):
        
        hh.append(y0 + const * ((i) **2 ) * Abbildung) 
        
    return hh
        #plt.plot(xp(x0), parabely(Zmax,x0))
        

    
#now plot:
    
img = mpimg.imread('20140131_012ions.jpg')

imshow(img)

lum_img = img[:, :]

imgplot = plt.imshow(lum_img)

# spectral, hot, cool, ... tip was falsches ein.. dann kommen vorschläge :)
imgplot.set_cmap('binary_r')

plt.plot(xp(x0),parabely(x0,ZA),"r")


# plot - loop for elements (carbon C12, CC, O16, 015, N14, N15...)

C12 = 1.0/12.0107 

C24 = 0.5/12.0107 

O16 = 1.0/15.9949 

O15 = 1.0/15.0031

N14 = 1.0/14.0067

N15 = 1.0/15.00011 

C13 = 1.0/13.03355

C17 = 1.0/16.0226

C14 = 1.0/14.0334 

C15 = 1.0/15.0106 

F19 = 1.0/18.9984
#CH=1.0/(1.007276*2+12.0107)
  
for i in range(2,6+1):

    #plt.plot(xp(x0), parabely(x0,C17*(i)),"y")
    #plt.plot(xp(x0), parabely(x0,O15*(i+1)),"y")
    #plt.plot(xp(x0), parabely(x0,C13*(i)),"g")
    #plt.plot(xp(x0), parabely(x0,C15*(i)),"r")
    #plt.plot(xp(x0), parabely(x0,C24*(i+6)),"y")
    #plt.plot(xp(x0), parabely(x0,C12*(i)),"w")
    plt.plot(xp(x0), parabely(x0,C12*(i)),"y")
    #plt.plot(xp(x0), parabely(x0,C12*(i)+0.0015),"y--")
    plt.plot(xp(x0), parabely(x0,O16*(i+1)),"b")
   # plt.plot(xp(x0), parabely(x0,O16*(i+1)+0.0015),"b--")
    #plt.plot(xp(x0), parabely(x0,N14*(i)),"g")
    #print parabely(x0,i)
    #plt.ylabel('C+',"i")0
    
plt.axis([0, 1032, 200, 756])


#plt.legend("+")
plt.show()



### 
raw_input('press Return>')


