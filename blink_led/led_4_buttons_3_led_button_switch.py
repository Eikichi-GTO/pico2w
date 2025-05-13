from machine import Pin
import time

led_pins = [Pin(15, Pin.OUT), Pin(16, Pin.OUT), Pin(17, Pin.OUT)]   
# Define the pin numbers for the LEDs
led_index = 0  # Index to track the current LED
# The initial index is set to 0, which corresponds to the first LED.

button_slow = Pin(14, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
button_fast = Pin(13, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
button_stop = Pin(12, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
button_on = Pin(11, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
button_led_switch = Pin(10, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor
# Initialize the button pins with pull-up resistors

mode = 0  # Initial mode (0: off, 1: slow blink, 2: fast blink, 3: on)
# The initial mode is set to off (0).
last_blink = time.ticks_ms()  # Timestamp for last blink
# The last blink time is initialized to the current time.
led_on = False  # Track LED state independently
# The LED state is tracked independently to ensure it can be turned on or off based on the mode.
blink_intervals = {0: 0, 1: 500, 2: 100, 3: 0} # Blink intervals for each mode
# The blink intervals for each mode are defined in a dictionary.
last_button_led_switch = 1
# The last button state is initialized to high (1).
# This variable will be used to detect button presses.

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
        
        # led switch
        current_button_led_switch = button_led_switch.value()
        # The current button state is read from the button pin.
        # If the button is pressed, it will read low (0), and if not pressed, it will read high (1).
        if current_button_led_switch == 0 and last_button_led_switch == 1:
            led_pins[led_index].value(0)  # Turn off the current LED
            led_on = False # Set LED state to off
            
            led_index = (led_index + 1) % len(led_pins)  # Move to the next LED
            time.sleep(0.2)  # Debounce delay
        last_button_led_switch = current_button_led_switch
        # Update the last button state to the current state
        
        # Blinking logic
        now = time.ticks_ms() # Get current time
        interval = blink_intervals[mode]   # Get the blink interval for the current mode
        
        if mode == 1 or mode == 2:
            if time.ticks_diff(now, last_blink) >= interval: # Check if it's time to blink
                led_on = not led_on # Toggle LED state
                led_pins[led_index].value(led_on) # Set LED to the new state
                last_blink = now
            
        elif mode == 3:
            led_pins[led_index].value(1)
            led_on = True
        
        else:
            for i in range(len(led_pins)):
                led_pins[i].value(0)
                # Turn off all LEDs
                # If not in blink mode, keep the LED off.
            led_on = False
        
        time.sleep(0.01)  # Small sleep to reduce CPU load

except KeyboardInterrupt:
    for led in led_pins:
        led.value(0)
    # Turn off all LEDs on stop
    # If the program is interrupted (e.g., by pressing Ctrl+C), all LEDs are turned off.

       