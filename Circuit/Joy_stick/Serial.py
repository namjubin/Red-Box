import serial

if __name__ == '__main__':
    ser = serial.Serial('com3', 9600, timeout=0.1)
    ser.flush()
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').rstrip()
            data = line
            print(data.split())