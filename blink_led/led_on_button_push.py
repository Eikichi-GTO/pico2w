# led_on_button_push.py - Raspberry Pi Pico 2W project
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
