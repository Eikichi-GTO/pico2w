# led_blink_on_push_on_off_2.py - Raspberry Pi Pico 2W project
# Copyright (C) 2025 Roman Molchanov
#
# This file is part of the pico2w collection.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_UP)

blink_mode = False
last_button = 1
last_blink = time.ticks_ms()  # Timestamp for last blink
blink_interval = 500  # Blink speed in milliseconds

led_on = False  # Track LED state independently

try:
    while True:
        current_button = button.value()

        # Detect button press edge
        if current_button == 0 and last_button == 1:
            blink_mode = not blink_mode
            time.sleep(0.2)  # Debounce

        last_button = current_button

        # Blinking logic
        if blink_mode:
            now = time.ticks_ms() # Get current time
            if time.ticks_diff(now, last_blink) >= blink_interval: # Check if it's time to blink
                led_on = not led_on # Toggle LED state
                led.value(led_on) # Set LED to the new state
                # Update last blink time
                last_blink = now
        else:
            led.value(0)
            led_on = False

        time.sleep(0.01)  # Small sleep to reduce CPU load

except KeyboardInterrupt:
    led.value(0)
