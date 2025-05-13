from machine import Pin
import time

# Define the pin numbers for the LED and button
led = Pin(15, Pin.OUT)  # LED pin
button_slow = Pin(14, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
button_fast = Pin(13, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
button_stop = Pin(12, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
button_on = Pin(11, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
# Initialize the button pins with pull-up resistors
# The button pins are set to input mode with pull-up resistors, which means they will read high (1) when not pressed and low (0) when pressed.
# The LED pin is set to output mode.

mode = 0  # Initial mode (0: off, 1: slow blink, 2: fast blink, 3: on)
# The initial mode is set to off (0).
# The code will toggle the LED state based on the button presses.

last_blink = time.ticks_ms()  # Timestamp for last blink
# The last blink time is initialized to the current time.
led_on = False  # Track LED state independently
# The LED state is tracked independently to ensure it can be turned on or off based on the mode.

blink_intervals = {0: 0, 1: 500, 2: 100, 3: 0} # Blink intervals for each mode
# The blink intervals for each mode are defined in a dictionary.
# Mode 0: off, Mode 1: slow blink, Mode 2: fast blink, Mode 3: on
# The blink intervals are in milliseconds.
try:
    while True:
        # button input
        if button_slow.value() == 0:  # Button pressed
            mode = 1
            time.sleep(0.2)
        
        if button_fast.value() == 0:  # Button pressed
            mode = 2
            time.sleep(0.2)
            
        if button_stop.value() == 0:  # Button pressed
            mode = 0
            time.sleep(0.2)
            
        if button_on.value() == 0:  # Button pressed
            mode = 3
            time.sleep(0.2)
        
        
        # Blinking logic
        now = time.ticks_ms() # Get current time
        interval = blink_intervals[mode]   # Get the blink interval for the current mode
        
        if mode == 1 or mode == 2:
            if time.ticks_diff(now, last_blink) >= interval: # Check if it's time to blink
                led_on = not led_on # Toggle LED state
                led.value(led_on) # Set LED to the new state
                last_blink = now
        elif mode == 3:
            led.value(1)
            led_on = True
        else:
            led.value(0)
            led_on = False
        
        time.sleep(0.01)  # Small sleep to reduce CPU load

except KeyboardInterrupt:
    led.value(0)
            
        