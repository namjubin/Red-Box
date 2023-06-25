import serial
           
ser = serial.Serial('com5', 9600, timeout=0.05)
ser.flush()
ser.close()