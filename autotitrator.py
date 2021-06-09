import math
import matplotlib.pyplot as plt
def give_vol(pH, list_pKas, V0, CHxA, CNaOH):
    list_pKas=sorted(list_pKas)
    H=10**(-1*pH)
    if len(list_pKas)==1:
        Ka1=10**(-1*list_pKas[0])
        denom=(H+Ka1)
        alpha_1=Ka1/denom
        alpha_2=0
        alpha_3=0
        alpha_4=0
    elif len(list_pKas)==2:
        Ka1=10**(-1*list_pKas[0])
        Ka2=10**(-1*list_pKas[1])
        denom=(H**2)+(H*Ka1)+(Ka1*Ka2)
        alpha_1=(H*Ka1)/denom
        alpha_2=(Ka1*Ka2)/denom
        alpha_3=0
        alpha_4=0
    elif len(list_pKas)==3:
        Ka1=10**(-1*list_pKas[0])
        Ka2=10**(-1*list_pKas[1])
        Ka3=10**(-1*list_pKas[2])
        denom=(H**3)+(Ka1*H**2)+(Ka1*Ka2*H)+(Ka1*Ka2*Ka3)
        alpha_1=(Ka1*H**2)/denom
        alpha_2=(Ka1*Ka2*H)/denom
        alpha_3=(Ka1*Ka2*Ka3)/denom
        alpha_4=0
    elif len(list_pKas)==4:
        Ka1=10**(-1*list_pKas[0])
        Ka2=10**(-1*list_pKas[1])
        Ka3=10**(-1*list_pKas[2])
        Ka4=10**(-1*list_pKas[3])
        denom=(H**4)+(Ka1*H**3)+(Ka1*Ka2*H**2)+(Ka1*Ka2*Ka3*H)+(Ka1*Ka2*Ka3*Ka4)
        alpha_1=(Ka1*H**3)/denom
        alpha_2=(Ka1*Ka2*H**2)/denom
        alpha_3=(Ka1*Ka2*Ka3*H)/denom
        alpha_4=(Ka1*Ka2*Ka3*Ka4)/denom
    else:
        return("ERROR: number of acidic protons not within limits of function (1-4)")
    
    sum_alphas=(alpha_1)+(2*alpha_2)+(3*alpha_3)+(4*alpha_4)
    sum_times_CHxA=sum_alphas*CHxA
    base_minus_acid=(10**(-14)/H)-H
    total_num=(sum_times_CHxA+base_minus_acid)*V0
    total_denom=CNaOH-base_minus_acid
    return total_num/total_denom
yval = []
xval = []
def titrate(pH, list_pKas, V0, CHxA, CNaOH):
    pH=(pH+0.1)
    if pH < 12:
        yval.append(pH)
        x = give_vol(pH, list_pKas, V0, CHxA, CNaOH)
        xval.append(x)
        titrate(pH, list_pKas, V0, CHxA, CNaOH)
        plt.xlabel("Vol added base (mL)")
        plt.ylabel("pH")
    return plt.plot(xval, yval)

titrate(2.0, [3, 2, 10, 5], 50, 0.05, 1) #enter data here
#Now data can be entered more freely.
#pH is automatically entered by the code
#within the brackets, enter 1-4 pKas in any order separated by commas
#Variable 3: Initial volume of acid in mL
#Variable 4: Initial concentration of acid in mol/L
#Variable 6: Concentration of Strong Base in mol/L