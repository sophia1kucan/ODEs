import math
import matplotlib

def foo(a):
    print(a)

if __name__ =='__main__':
    print('123')
    foo(234)

    for i in range (10000):
        j = i*i*3.14159268
        k = math.sqrt(j*j*j*j)
        print(j)
