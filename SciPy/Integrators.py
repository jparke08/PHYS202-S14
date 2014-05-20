#%pylab inline
import numpy as np
def trapz(func,a,b,N):
    """ Integrates a function from a to b with N 
    slices using trapezoidal rule"""
    a = float(a)
    b = float(b)
    h = (b-a)/N

    k = np.arange(1,N)
    return h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())

def simps(func,a,b,N):
    """ Integrates a function from a to b with N
    slices using Simpson's rule"""
    a = float(a)
    b = float(b)
    h = (b-a)/N

    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    return (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())