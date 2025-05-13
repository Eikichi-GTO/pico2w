from machine import Pin
import time

led = Pin(15, Pin.OUT)

try:
    while True:
        led.toggle()
        time.sleep(0.5)
except KeyboardInterrupt:
    led.value(0)  # turn off LED on stop