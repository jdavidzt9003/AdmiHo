from machine import Pin, TouchPad
import time
huella = TouchPad(Pin(4));

LED23 = Pin(15, mode=Pin.OUT, value=0) # se inicializa el GPIO23 como salida del LED23 y se deja apagado
tiempoLimite = time.ticks_add(time.ticks_ms(), 100)     # se define la variable tiempoLimite para comprobar T0
                                                        # tiempo RTC + 100 ms
while True:
    if time.ticks_diff(tiempoLimite, time.ticks_ms()) <= 0: # se compruebas si el tiempoLimite se ha agotado
        if T0.read()<300:             # si el tiempo se ha agotado y T0 tiene contacto...                            
            LED23.on()                # ... se enciende el LED
        else:                         # si el tiempo se ha agotado y T0 no tiene contacto...
            LED23.off()               # ...se apaga el LED
        
        tiempoLimite = time.ticks_add(time.ticks_ms(), 100)