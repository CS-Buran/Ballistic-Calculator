import numpy as np;

def calculateTime(v, x):
    t = x/v
    return t

def calculateNoDrag(v, t):
    x = v*t
    return x 

def dragFormula(Cd, Ro, A, v, t,  m):
    drag = -((Cd * Ro * A * np.square(v) * np.square(t)) / 2*m)

    return drag

def dragFormAccel(Cd, Ro, A, v,  m):
    drag = -((Cd * Ro * A * np.square(v)) / (2*m))
    return drag

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


def decelCalc(vi, t, dc):

    vf = (dc * t) + vi
    return vf


print("Select operation.")
print("1.Calculate Drop")
print("2.Calcualte Correction")

print("0.Exit")
print("")

while True:
    choice = input("Enter 1, 2 or 0  ")
    if choice in ('1' , '2', '0'):
        if choice == '0':
            break
        
        if choice == '1':
            num1 = float(input("Enter speed m/s "))
            #num2 = float(input("Enter height meters "))
            num2 = -0.05
            num3 = 9.81
            #num4 = float(input("Enter BC  "))
            #num4 = 0.496
            #num5 = float(input("Enter air density kg/m^3 "))
            #num5 = 1.2
            #num6 = float(input("Enter Cross Sectional Area m^2 "))
            #num6 = 0.000048
            #num7 = float(input("Enter weight of bullet in grains  "))
            #num7 = 175
            num8 = float(input("Enter shot distance  "))

            #zero = float(input("Enter zero distance  "))
            zero = 91.44

            #zeroCorr = angleCalc(zero + dragFormula( num4,num5,num6,zero,calculateTime(num1,zero), grainToKilo(num7)),num1,num2,num3)
            #angle = angleCalc(num8 + dragFormula( num4,num5,num6,num1,calculateTime(num1,num8), grainToKilo(num7)),num1,num2,num3)

            zeroCorr = angleCalc(zero ,num1,num2,num3)
            angle = angleCalc(num8 ,num1,num2,num3)

            withCorr = angle - zeroCorr

            

            print(toMills(withCorr))

        if choice == '2':
            num1 = float(input("Enter speed m/s "))
            #num4 = float(input("Enter BC  "))
            num4 = 0.4
            #num5 = float(input("Enter air density kg/m^3 "))
            #num5 = 1.2
            num5 = 1.15
            #num6 = float(input("Enter Cross Sectional Area m^2 "))
            num6 = 0.000048
            #num7 = float(input("Enter weight of bullet in grains  "))
            num7 = 175 
            num8 = float(input("Enter shot distance  "))
            
            totalTime = 3
            distance = 0
            timeInFlight = 0
            initialvelocity = num1
            #dr = dragFormula(num4, num5, num6, num1, grainToKilo(num7))

            while totalTime>0 and num1 > 273 and distance < num8:
                dr = dragFormAccel(num4, num5, num6, num1, grainToKilo(num7))

                velocity = decelCalc(num1, 0.001, dr)
                num1 = velocity
                instantDistance = 0.001*num1

                distance += instantDistance
                timeInFlight += 0.001

                print(dr, " m/s^2")
                print(velocity, " m/s")
                print(distance, " m")
                print(timeInFlight, " s")
                print("               ")
                totalTime -= 0.001

            correction = timeInFlight*initialvelocity
            print("Done")
            print("Corrected shot distance =  ", correction )
            print("")
            print("")
            #step distance not a problem, in both cases ( 0.001 of a sec and 0.00001 of a sec) the speed is underestimated by a bit more than 100m/s 
            #supposed to be 1800 ft/s or 548.64 at 500 yards or 457.2 meters
            #actually is 1461.6 ft/s or 445.5 m/s 

    
    else:
        print(" Invalid num");
        print( "")