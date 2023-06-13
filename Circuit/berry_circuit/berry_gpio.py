try:
    import RPi.GPIO as GPIO
except:
    print("Error importing RPi.GPIO!\nThis is probably because you need superuser privileges.\nYou can achieve this by using 'sudo' to run your script")

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pin = 18
trig = 23
echo = 24

