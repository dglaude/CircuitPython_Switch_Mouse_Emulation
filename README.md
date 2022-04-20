# CircuitPython_Switch_Mouse_Emulation

This is a non working tentative to emulate mouse on the Nintendo Switch.
This code is made to be running on Adafruit MacroPad: https://learn.adafruit.com/adafruit-macropad-rp2040 (mostly because it has button, rotary encoder and USB-C)

I took code from this learn guide: https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse
And many advice from this learn guide: https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial
Rotary encoder code from TodBot: https://github.com/todbot/circuitpython-tricks#read-a-rotary-encoder

Right now I have disabled:
* Mass storage
* CDC Serial
* MIDI

If you need to access those to modify the code, press the bottom right button (button 12) at boot/restart.

Right now this is a total failure...

The switch that detect a real mouse without issue (in "Game Builder Garage") but not when I connect my MacroPad.

Next step is to remove keyboard and Customer_Control from the composite HID so that only mouse is left:
https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices

If that fail, then I will call for help on the Circuit Python community.
