# coding: utf-8
import matplotlib.pyplot as plt
import defUpc as cal
plt.style.use('bmh')
import numpy as np
import math
import os

#Datos:
Md = 2114     # Momento en Kn.m a (tn.m / 10)
Fyk = 500   # Fluencia en Mpa o N/mm2
Fck = 40    # Momento en Mpa o N/mm2

H = 0.70    # Canto en m
B = 0.40    # Base en m

Rnon = 20     # REcubrimiento nominal mm
Al = 25       # Diametro Acero Longitudonal mm
At = 10       # Diametro Acero Tranversal mm

Ys = 1.15   # Factor de - Acero
Yc = 1.5    # Factor de - Concreto
Tma = 20    # Tamaño maximo agregado en mm

Rmec = (Rnon + At + 0.5 * Al)/1000    # Recubrimirnto mecanico mt
D = H - Rmec

# n en zona de conpresion seguna ACI 0.85 f'c
nfc = cal.n(Fck)
Yfc = cal.Y(Fck)
Fcd = Fck/Yc
Fyd = Fyk/Ys
#Xlim en mt
xlim = (cal.Ecu(Fck)/(Fyk/(Ys*200000) + cal.Ecu(Fck))) * D
ylim = xlim * Yfc

#print(ylim)

uo = nfc * Fcd * 1000 * B * D    #Aporte en toda la zona de compresion
fclim = ylim * nfc * Fcd * 1000 * B   # En Kn
mlim = fclim * (D - 0.5 * ylim)  # Mometo a Conpresion

a = nfc * Fcd * 1000 * B * 0.5
b = -nfc * Fcd * 1000 * B * D
c = Md

y = (-b - math.sqrt(b**2 - 4 * a * c))/(2 * a)

# Area de acero minimo mecanica
Asmin_mec = 0.04 * B * H * Fcd / Fyd * 1e4

# Area acero minimo Geometrico
Asmin_geo = cal.Pasmin(Fyk, 'Vigas') * B * H * 1e4

# Area acero minimo Geometrico
Asmin = max(Asmin_mec, Asmin_geo)

# Area acero minimo Geometrico*0.3
Asmin_Con = Asmin / 3

if Md < mlim and y > 0 and y < H :
    y = (-b - math.sqrt(b ** 2 - 4 * a * c))/(2 * a)
    x = y / Yfc
    Fc = nfc * Fcd * 1000 * B * y

    # Area de acero
    As = y * nfc * Fcd * B * 10000 / (Fyd)

    # Area de Acero redondeado
    As_Redon = math.ceil(As * 5) / 5

    # Distribucion
    nvl = As / (math.pi * 0.25 * (Al / 10) ** 2)

    # Base efectiva mm
    be = B * 1000 - 2 * (Rnon + At)

    # Separacion Diametrolon, Tma, vibrado en mm
    sep = cal.Sepa(Al, Tma, 20)

    # Fila ingresan
    nfil = (be + sep) / (sep + Al)

    nfil_entero = math.floor(nfil)

    # As por fila
    As_Fila = nfil_entero * math.pi * 0.25 * (Al / 10) ** 2

    # print(Asmin)
    As_diseno = max(Asmin, As)

    print("****************************************")
    print("* Universidad Nacional de Huancavelica *")
    print("*    Facultad Ciencias de Ingeniería   *")
    print("*         E.A.P Ingeniería Civil       *")
    print("****************************************\n")
    print(" !Calculo de Canto Util!")
    print(u"        Hormigón")
    print("")
    print("*Canto D     = {0:.3f} cm".format(D * 100))
    print("*X lim       = {0:.3f} cm".format(xlim * 100))
    print("*Y lim       = {0:.3f} cm".format(ylim * 100))
    print("*U0          = {0:.3f} kn".format(uo))
    print("*Fc lim      = {0:.3f} kn".format(fclim))
    print("*Mn lim      = {0:.3f} kn.m".format(mlim))
    print("*Zona C(Y)   = {0:.3f} m".format(y))
    print("*Eje N(X)    = {0:.3f} m".format(x))
    print("*Fc Act      = {0:.3f} Kn".format(Fc))
    print("*Area Acero  = {0:.3f} cm2".format(As))
    print("*As Redonde  = {0:.3f} cm2".format(As_Redon))
    print("*Asmi Mecan  = {0:.3f} cm2".format(Asmin_mec))
    print("*Asmi Geome  = {0:.3f} cm2".format(Asmin_geo))
    print("*Asminimo    = {0:.3f} cm2".format(Asmin))
    if Asmin < As:
        print("*AsDiseño   = {0:.3f} cm2".format(As_Redon))
    else:
        print("*AsDiseño   = {0:.3f} cm2".format(Asmin))

    print("*AsTraccion    = {0:.3f} cm2".format(Asmin_Con))
    print("*Separacion    = {0:.2f} mm".format(sep))
    print("*Base (B')     = {0:.2f} mm".format(be))
    print("*Fila de D     = {0:.2f} und".format(nfil))
    print("*F Redonde     = {0:.2f} und".format(nfil_entero))
    print("*AS.FIla       = {0:.2f} und".format(As_Fila))
    if As < As_Fila:
        print("*Ingresa en una sola Fila")
    else:
        Nfilas = As_diseno / As_Fila
        print("*Ingresan en = {0:.2f} unds".format(Nfilas))

    print("*Numero As   =", round(nvl, 2), " de ", str(Al), 'mm2', '@', str(sep), 'mm')

else:
    Dd = Rmec
    print("Analizar Acero en Traccion")
    As = fclim/Fyd*10
    #Area de acero As2
    As2 = (Md - mlim)*10/((D-Dd)*Fyd)
    #Area de caero As1 en traccion
    As1 = As + As2
    #Area de caero As1 en traccion
    As1_Redon = math.ceil(As1 * 5) / 5

    print("****************************************")
    print("* Universidad Nacional de Huancavelica *")
    print("*    Facultad Ciencias de Ingeniería   *")
    print("*         E.A.P Ingeniería Civil       *")
    print("****************************************\n")
    print(" !Calculo de Acero Longitudinal!")
    print(u"        Hormigón")
    print("")
    print("*Canto D       = {0:.3f} cm".format(D * 100))
    print("*X lim         = {0:.3f} cm".format(xlim * 100))
    print("*Y lim         = {0:.3f} cm".format(ylim * 100))
    print("*U0            = {0:.3f} kn".format(uo))
    print("*Fc lim        = {0:.3f} kn".format(fclim))
    print("*Mn lim        = {0:.3f} kn.m".format(mlim))
    print("*Zona C(Y)     = {0:.3f} m".format(y))
    #print("*Eje N(X)      = {0:.3f} m".format(x))
    #print("*Fc Act        = {0:.3f} Kn".format(Fc))
    print("*AsLim         = {0:.3f} cm2".format(As))
    print("*Area Acero    = {0:.3f} cm2".format(As1))
    print("*As1 Redonde   = {0:.3f} cm2".format(As1_Redon))
    print("*As2 Traccion  = {0:.3f} cm2".format(As2))
    print("*Asmi Mecan    = {0:.3f} cm2".format(Asmin_mec))
    print("*Asmi Geome    = {0:.3f} cm2".format(Asmin_geo))
    print("*Asminimo      = {0:.3f} cm2".format(Asmin))



















