import board
import time
import digitalio
import neopixel

# create a neopixel object for 10 pixels
pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1, auto_write=False)

# declare inputs for button A and B
button_A = digitalio.DigitalInOut(board.BUTTON_A)
button_A.switch_to_input(pull=digitalio.Pull.DOWN)
button_B = digitalio.DigitalInOut(board.BUTTON_B)
button_B.switch_to_input(pull=digitalio.Pull.DOWN)

# declare colors variables
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

# set color variables in 'colors' object
colors = [OFF, RED, YELLOW, GREEN, CYAN, BLUE, PURPLE, WHITE]

# declare initial states and set variable values
button_a_start = button_A.value
button_b_start = button_B.value
press_count = 0
hold_mode = False
brightness_val = 1.0
brightness_inc = +0.1

while True:
    # gather input values
    button_a_read = button_A.value
    button_b_read = button_B.value

    # output for button A
    if button_a_read:
        hold_mode = True
    else:
        hold_mode = False

    # output for button A when held
    if hold_mode:
        brightness_val += brightness_inc
        if brightness_val <= 0:
            brightness_val = 0
            brightness_inc = 0.1
        elif brightness_val >= 1.0:
            brightness_val = 1.0
            brightness_inc = -0.1
        pixels.brightness = brightness_val
    else:
        pixels.fill(colors[press_count])

    # output for button B
    if button_b_read:
        press_count += 1
        if press_count > 7:
            press_count = 0
        print(press_count)

    pixels.show()
    time.sleep(0.1)
