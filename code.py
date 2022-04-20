# From: https://github.com/todbot/circuitpython-tricks
# Detect if USB is connected or not
import supervisor
import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

import rotaryio

from digitalio import DigitalInOut,Pull

led = DigitalInOut(board.LED)
led.switch_to_output()

led.value = False

if supervisor.runtime.usb_connected:
  led.value = True   # USB
  print("Connected")
else:
  led.value = False  # no USB
  print("NOT Connected")

# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Mouse example"""

mouse = Mouse(usb_hid.devices)

select = digitalio.DigitalInOut(board.BUTTON)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP

encoder = rotaryio.IncrementalEncoder(board.ENCODER_A, board.ENCODER_B) # must be consecutive on Pico

while True:
    led.value = not select.value
    print(encoder.position)  # starts at zero, goes neg or pos
    mouse.move(x=-encoder.position)
    if select.value is False:
        mouse.click(Mouse.LEFT_BUTTON)
    time.sleep(0.2)  # Debounce delay
