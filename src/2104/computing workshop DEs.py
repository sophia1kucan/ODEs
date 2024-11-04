#import numpy as np
#import scipy.integrate as sp
#import matplotlib.pyplot as mat

    
def recursivesequence(a0, a1, N):
    an = [a0, a1]
    for n in range(0, N - 2):
        an2 = (a0/((n + 1)(n + 2)) - (n/(n/2)) * a1)
        an.append(an2)
    return an
   




    




