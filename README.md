# Thomson-Parabola-analytical-plot
plots Parabolas for different Z/A values for testing the spectrometer function

============================================
Thomson spectrometer consists of static magnitic field (hier parallel to x) and static 
electric field in y direction. Charge ions that pass it are deflected in their velocity 
(the faster the closer to the cero point) and separeted in different traces according 
to their charge to mass ratio (Z/A). 
Usually the parameters of the spectrometer can be measured within a certain accuracy. 
This programm displays the parabolas for different Z/A ratios (light ions, H, C, 0)
on a recorded image of the detector. By this deviations in E and B, or D can be seen, 
when the theoretical plots do not match to experimental one.


function: f(y) = y0 + (mp * EF / (Z/A *q * l * D * B ** 2)) * x**2 * Abbildung.

y0, x0 - cero point of parabola, in px.
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

