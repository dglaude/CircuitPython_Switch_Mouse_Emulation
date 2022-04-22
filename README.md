# CircuitPython_Switch_Mouse_Emulation

This is a non working tentative to emulate mouse on the Nintendo Switch.
This code is made to be running on Adafruit MacroPad: https://learn.adafruit.com/adafruit-macropad-rp2040 (mostly because it has button, rotary encoder and USB-C)
The code is implementing a 1D mouse that can only go left or right with the rotary encoder, and left click (also with the rotary encoder).

I took code from this learn guide: https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse
And many advice from this learn guide: https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/circuitpy-midi-serial
Rotary encoder code from TodBot: https://github.com/todbot/circuitpython-tricks#read-a-rotary-encoder

Right now I have disabled:
* Mass storage
* CDC Serial
* MIDI

I have also removed keyboard and Customer_Control from the composite HID so that only mouse is left:
* https://learn.adafruit.com/customizing-usb-devices-in-circuitpython/hid-devices

The switch that detect a real mouse without issue (in "Game Builder Garage") but not detect the MacroPad as a mouse.
My PC detect that properly as a mouse.

The solution to make the Switch detect a CircuitPython device as a mouse is to define a custom USB-HID.
I first attempted to replicate a custom USB-HID for an absolute mouse within this repo: https://github.com/dglaude/CircuitPython_udraw_Absolute_Mouse
That absolute mouse is working on Windows, but the Switch (in "Game Builder Garage) does not react properly.
It is detect a mouse (display a mouse pointer), but at first move it is stuck for ever at the bottom left of the screen.

So once I had that working, I needed to modify the custom USB-HID for one of a normal mouse.
This is done and working in this repo: https://github.com/dglaude/Wii_uDraw_for_Nintendo_Switch

PS: If you need to access those to modify the code, press the bottom right button (button 12) at boot/restart.
