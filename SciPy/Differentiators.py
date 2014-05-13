
import numpy as np

def twoPtForwardDiff(x,y):
    """Returns the derivative of a function by
    finding the slope between consecutive points"""
    
    dydx = np.zeros(y.shape,float)
    
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dydx


def twoPtCenteredDiff(x,y):
    """Returns the derivative of a function by
    finding the slope at each x-value"""
    
    dydx = np.zeros(y.shape,float)
    
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2]) #center difference
    
    dydx[0] = (y[1]-y[0])/(x[1]-x[0]) #forward difference
    
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2]) #backward difference
    
    return dydx

def fourPtCenteredDiff(x,y):
    """Returns  derivative of a function by
    using a four-point differencing method"""
    
    dydx = np.zeros(y.shape,float)
    
    dydx[0] = (y[1]-y[0])/(x[1]-x[0])
    
    dydx[1] = (y[2]-y[0])/(x[2]-x[0])
    
    dydx[2:-2] = (y[:-4]-8*y[1:-3]+8*y[3:-1]-y[4:])/(12*np.diff(x)[0])
    
    dydx[-2] = (y[-1]-y[-3])/(x[-1]-x[-3])
    
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    
    return dydx