import storage, usb_cdc
import board, digitalio
import usb_hid, usb_midi

# On the Macropad, pressing a key grounds it. You need to set a pull-up.
# If not pressed, the key will be at +V (due to the pull-up).
button = digitalio.DigitalInOut(board.KEY12)
button.pull = digitalio.Pull.UP

# Disable devices only if button is not pressed.
if button.value:
    storage.disable_usb_drive()
    print("storage.disable_usb_drive()")
    usb_cdc.disable()
    print("usb_cdc.disable()")
    usb_midi.disable()
    print("usb_midi.disable()")
    usb_hid.enable()
    print("usb_hid.enable()")
    usb_hid.enable((usb_hid.Device.MOUSE,))       # Enable just MOUSE.
    print("usb_hid.enable((usb_hid.Device.MOUSE,))")

print("End of boot.py")
