import numpy as np

def oneDtoTwoD(x,y):
    reversedX = x[::-1]
    reversedY = y[::-1]

    arr = np.column_stack((reversedX, reversedY))
    return arr


def ourDragCoefficient(m, arr, cal, BC):
    #m - mass of bullet in grains
    #arr - array of standard bullet(G1/G7) drag coeffiecients
    #cal - Bullet Calliber
    #BC - Ballistic coefficient (G1/G7)
    l = [0] * 69
    cdArr = np.asarray(l)
    n=0
    while((arr.size-1) >= n):
        top = m * arr[n]
        btm = np.square(cal) * BC * 7000
        cd = top/btm
        cdArr[n] = str(round(cd, 4))
        n+=1

    return cdArr

def dragFormula(dc, Ro, A, v, t,  m):
    drag = -((dc * Ro * A * np.square(v) * np.square(t)) / 2*m)

    #dc - drag coefficient
    #Ro - air density
    #v - velocity in m/s
    #t - time 
    #m - mass of bullet in grains

    return drag

def dragFormAccel(dc, Ro, A, v,  m):
    drag = -((dc * Ro * A * np.square(v)) / (2*m))

    #dc - drag coefficient
    #Ro - air density
    #v - velocity in m/s
    #m - mass of bullet in grains

    return drag

def decelCalc(vi, t, dc):
    vf = (dc * t) + vi

    #vf - velocity final
    #vi - velocity initial
    #dc - drag coefficient
    return vf

def grainToKilo(grain):
    kilo = grain * 0.0000647989
    return kilo



def angleCalc(x, v0, y0, g):
    a = ((g*np.square(x))/(np.square(v0)))
    b = np.sqrt(np.square(y0) + np.square(x))
    c = x/y0
    d = (a-y0)/b

    deg1 = np.degrees(np.arccos(d))
    deg2 = np.degrees(np.arctan(c))
    theta = (deg1+deg2)/2
    
    return theta

def toMills(angle):
    mills = angle/0.05625
    return mills

def toMachNumber(v):
    #v = meters per second
    machNumber = v * 0.002915
    return machNumber


def bestMatch(v, arr):
    #v - velocity in mach number
    #arr - 2d array of drag coefficient corresponding to mach number for particular bullet

    dragCoefficient = (np.abs(arr - v)).argmin()
    return arr[dragCoefficient]