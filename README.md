# Four Shinobi (python)
 Plotting graph of Acceleration , Velocity and Displacement using ADXL345 and Python

We are focused on sending data from the Arduino to computer over serial connection, and then plotting it with Python.
The Python portion is not simple as the Arduino's one. We uesd custom class to handle the data from Arduino and then use matplotlib to plot the graphs in real time.In order to send/retrieve data, we require another package called pySerial.
Installation instruction for pySerial :
 pip install pyserial

We are going to deal with the Serial data and plotting separately.In order to plot real time data, we have to read data(most updated values) as fast as possible.
In this python code, we are taking few finite inputs and plotting it. But we can also read continuous data and real time plotting also can be done using while loop or thread concept.
Python code is given for plotting of Acceleration, Velocity and Displacement in all three direction.
