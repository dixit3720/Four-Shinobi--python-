from turtle import color
import serial
import time 
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from drawnow import *

#acceleration variables
xData=[]
yData=[]
zData=[]

# velocity variables
vX=[0]
vY=[0]
vZ=[0]
# displacement variables
dX=[0]
dY=[0]
dZ=[0]

# conneting to port
serialObj=serial.Serial('COM7')
serialObj.close()
serialObj.open()
serialPort='COM7'
serialBaud= 9600
plt.ion()   #Tell matplotlib you want interactive mode to plot live data
fig = plt.figure()
print('Trying to connect to: ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')


# try:
#     serialConnection = serial.Serial(serialPort, serialBaud)
#     print('Connected to ' + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')
# except:
#     print("Failed to connect with " + str(serialPort) + ' at ' + str(serialBaud) + ' BAUD.')



def plottingGraph():
    # plotInterval = 50 # period at which the plot animation updates (ms)

    plt.subplot(3,1,1) # row column plot nos.
    plt.plot(xData,color='r')
    plt.plot(yData,color='g')
    plt.plot(zData,color='b')
    plt.legend(["x","y","z"])
    plt.title("Acceleration",loc="right")
    plt.ylabel("m/s^2")
    plt.xlabel("t")
    plt.grid()

    plt.subplot(3,1,2)
    plt.plot(vX,color='r')
    plt.plot(vY,color='g')
    plt.plot(vZ,color='b')
    plt.legend(["x","y","z"])
    plt.title("Velocity",loc="right")
    plt.ylabel("m/s")
    plt.xlabel("t")
    plt.grid()

    plt.subplot(3,1,3)
    plt.plot(dX,color='r')
    plt.plot(dY,color='g')
    plt.plot(dZ,color='b')
    plt.legend(["x","y","z"])
    plt.title("Displacement",loc="right")
    plt.ylabel("m")
    plt.xlabel("t")
    plt.grid()

    plt.show()


dt=float(2)
# i=0
#while True:  to plot continuous reading 
for i in range(100): # takes only few readings
    
    
    x= float(serialObj.readline())
    y= float(serialObj.readline())
    z= float(serialObj.readline())
    xData.append(x)
    yData.append(y)
    zData.append(z)

    # inputs for velocity
    vx=vX[i]+ xData[i]*dt
    vy=vY[i]+ yData[i]*dt
    vz=vZ[i]+ (zData[i]-9.8)*dt
    vX.append(vx)
    vY.append(vy)
    vZ.append(vz)
    # inputs for displacement
    dx=dX[i]+ vX[i]*dt
    dy=dY[i]+ vY[i]*dt
    dz=dZ[i]+ (vZ[i]-9.8)*dt
    dX.append(dx)
    dY.append(dy)
    dZ.append(dz)
    # i+=1
    drawnow(plottingGraph)
    plt.pause(.00001)
    
