# Four Shinobi (python)
 Plotting graph of Acceleration , Velocity and Displacement using ADXL345 and Python

Our team focuses on sending data from the ADXL345 sensor via Arduino to computer with the help 0f I2C serial connection, and then plotting the respective graphs using Python.
The Python code is not as simple as the Arduino's serial plotter.Hence, we uesd custom modules to handle the data from Arduino IDE and then used matplotlib library to plot the graphs in real time.In order to send/retrieve data, we required another package called pySerial.
Installation instruction for pySerial :
 pip install pyserial

In this problem we dealt with plotting as well as redistribution of real time data.
Continuous data serialization can be achieved using an infinite while loop or using thread concept.
