# coding: utf-8
#import androidhelper
import defUpc as cal
import math
import os
#Datos:
Md = 2114     # Momento en Kn.m a (tn.m / 10)
B = 0.4     # Base en m
Fck = 40     # Momento en Mpa o N/mm2
Fyk = 500    # Momento en Mpa o N/mm2

Al = 25      # Acero Logitudinal mm
At = 10      # Acero Tranversal mm
Re = 20      # Recubrimiento nominal mm

Ys = 1.15   # Factor de - Acero
Yc = 1.5    # Factor de - Concreto

#Calclumamos la distancao de la compresion
fcd = Fck / Yc
Ec = cal.Ecu(Fck)
Es = Fyk/(Ys*200000)
Lamda = cal.Y(Fck)

r = Ec/(Ec + Es) * Lamda
d = math.sqrt(Md/((1 - 0.5 * r) * cal.n(Fck) * fcd*1000 * B * r))
#Determina el Canto
H = cal.Canto(d,Re,Al,At)
print (d)


d1 = math.sqrt(Md/(cal.n(Fck) * fcd *1000 * B * 0.375))
H1 = cal.Canto(d,Re,Al,At)
print(d1)

#Reporte


# In[13]:
print("****************************************")
print("* Universidad Nacional de Huancavelica *")
print("*    Facultad Ciencias de Ingeniería   *")
print("*         E.A.P Ingeniería Civil       *")
print("****************************************\n")
print(" !Calculo de Canto Util!")
print("        Hidraulica")
print("")
print("*Fyd  = {0:.3f} Mpa".format(fcd))
print("**d   = {0:.3f} mt".format(d))
print("**H   = {0:.3f} mt".format(H))
print("*H =", math.ceil(H*5)/5, " mt")

print("Formula y =  0.5*d")
print("________________________")
print("**d   = {0:.3f} mt".format(d1))
print("**H   = {0:.3f} mt".format(H1))
print("*H =", math.ceil(H1*5)/5, " mt")