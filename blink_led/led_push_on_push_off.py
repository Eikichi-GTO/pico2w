from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Button pin with pull-up resistor   
# Initialize the button pin with pull-up resistor
# The button pin is set to input mode with a pull-up resistor, which means it will read high (1) when not pressed and low (0) when pressed.
# The LED pin is set to output mode.

led_state = False  # Initial state of the LED
# The initial state of the LED is set to off (False).
# The code will toggle the LED state when the button is pressed.
last_button = 1
# The last button state is initialized to high (1).
# This variable will be used to detect button presses.

try:
    while True:
        current_button = button.value()  # Read the current button state
        # The current button state is read from the button pin.
        # If the button is pressed, it will read low (0), and if not pressed, it will read high (1).
        
        if current_button == 0 and last_button == 1:  # Button pressed
            led_state = not led_state  # Toggle LED state
            led.value(led_state)  # Set LED to the new state
            time.sleep(0.2)  # Debounce delay
            # A debounce delay is added to prevent multiple toggles from a single press.
        last_button = current_button
        # Update the last button state to the current state
        # This ensures that the next iteration will correctly detect the button press.
except KeyboardInterrupt:
    led.value(0)  # Turn off LED on stop
    # If the program is interrupted (e.g., by pressing Ctrl+C), the LED is turned off.
    
