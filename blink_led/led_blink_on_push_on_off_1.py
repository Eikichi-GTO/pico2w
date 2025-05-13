from machine import Pin
import time

# Define the pin numbers for the LED and button
led = Pin(15, Pin.OUT)  # LED pin
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor

blink_mode = False  # Flag to indicate blink mode.
# The initial state of the LED is set to off (False).
last_button = 1  # Last button state initialized to high (1)

try:
    while True:
        current_button = button.value()  # Read the current button state
        # The current button state is read from the button pin.
        # If the button is pressed, it will read low (0), and if not pressed, it will read high (1).
        
        if current_button == 0 and last_button == 1:  # Button pressed
            blink_mode = not blink_mode  # Toggle LED state
            time.sleep(0.2)
            # A debounce delay is added to prevent multiple toggles from a single press.
        if blink_mode:
            led.toggle()  # Toggle LED state
            time.sleep(0.5) # Blink delay
        else:
            led.value(0)  # Turn off LED
            # If not in blink mode, keep the LED off.    
except KeyboardInterrupt:
    led.value(0)  # Turn off LED on stop
    # If the program is interrupted (e.g., by pressing Ctrl+C), the LED is turned off.