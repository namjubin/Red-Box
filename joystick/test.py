import serial.tools.list_ports as sp

list = sp.comports()

for i in list:
    print(i.device)