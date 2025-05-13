from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor

try:
    while True:
        if not button.value():  # Button pressed (active low)
            led.value(1)  # Turn on LED
        else:
            led.value(0)
        time.sleep(0.1)
except KeyboardInterrupt:
    led.value(0)  # Turn off LED on stop
# This code will turn on the LED when the button is pressed and turn it off when released.
