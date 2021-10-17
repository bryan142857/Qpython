def n(fck):
    "Determina el coeficiente para fck zona compresion"
    if fck <= 50:
        n = 1
    elif fck > 50 and fck <= 90:
        n = 1 - (fck - 50)/200
    else:
        n = None
    return n

def Y(fck):
    """ Determina lamba en funcion del fck e Mpa o N/mm2"""
    if fck <= 50:
        Y = 0.8
    elif fck > 50 and fck <= 90:
        Y = 0.8 - (fck - 50)/400
    else:
        Y = None
    return Y

def Ecu(fck):
    "Deformacion unitaria del concreto a deformacion ultima"
    if fck <= 50:
        ecu = 0.0035
    elif fck > 50:
        #ecu = (2.6 + 35 * ((90 - fck)/100)**4)/1000 #SAp CfD-Ec-2-2004
        ecu = 0.0026 + 0.0144*((100-fck)/100)**4
    return ecu

def EcuRotu(fck):
    "Deformacion unitaria del concreto a deformacion ultima"
    if fck <= 50:
        ecu = 0.002
    elif fck > 50:
        ecu = 0.002 + 8.5 * 10**-5 * (fck-50)**0.5
    return ecu


def Canto(d,r,l,t):
    """ Determina el canto donde d en mt y l y t en mm"""
    return d + (0.5*l + t + r)/1000

def Pasmin (Fyk, Type ='Vigas'):
    if Fyk == 400:
        if Type == 'Pilares':
            asmin = 4
        elif Type == 'Losas':
            asmin = 2
        elif Type == 'Vigas':
            asmin = 3.3

    if Fyk == 500:
        if Type == 'Pilares':
            asmin = 4
        elif Type == 'Losas':
            asmin = 1.8
        elif Type =='Vigas':
            asmin = 2.8

    cmin = asmin/1000
    return cmin

def Sepa (Dl, Tma=20, V=20):
    S_Dl = Dl
    S_Tma = 1.25 * Tma
    S_V = V
    return max(S_Dl, S_Tma, S_V)








def xdlim (fck, s=1):
    k1 = 0.44
    k2 = 1.25 * (0.6 + 0.0014/Ecu(fck))
    k3 = 0.54
    k4 = 1.25 * (0.6 + 0.0014/Ecu(fck))
    "Definimos x/d limite"
    if fck <= 50:
        xdl = (s - k1) / k2
    elif fck > 50:
        xdl = (s - k3) / k4
    return xdl