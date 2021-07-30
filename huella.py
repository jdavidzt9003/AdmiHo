from machine import TouchPad
from machine import Pin
import time

led = Pin(15, Pin.OUT)    # create output pin on GPIO0
led.on()                 # set pin to "on" (high) level
led.off()                # set pin to "off" (low) level
led.value(1)


#t = TouchPad(Pin(4, Pin.IN))
#t.read()

huella = Pin(4, Pin.IN, Pin.PULL_DOWN)

while True:
    if huella.value()==1:
        print("Huella detectada")
        time.sleep(5)
    else:
        print("NO se ha detectado huella")
        time.sleep(5)