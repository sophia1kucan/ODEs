#import numpy as np
#import scipy.integrate as sp
#import matplotlib.pyplot as mat

    
# def recursive_sequence(a0, a1, N):
#     an = [a0, a1]
#     for n in range(0, N - 2):
#         an2 = 1#(a0/((n + 1)*(n + 2)) - (n/(n/2)) * a1)
#         an.append(an2)
#     return an

def recursive_sequence(a0, a1, N):
    res = []
    a_nm2, a_nm1 = a0, a1
    for n in range(0, N):
        an2 = a_nm2/((n + 1)*(n + 2)) - n/(n+2) * a_nm1
        res.append(an2)
        a_nm2 = a_nm1
        a_nm1 = an2
    return res

if __name__ =='__main__':
    seq = recursive_sequence(1, 1, 5)
    
    pass
   