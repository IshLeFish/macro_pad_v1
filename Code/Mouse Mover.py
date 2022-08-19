print("Hello World!")
import time
import digitalio
import board
import usb_hid

from adafruit_hid.mouse import Mouse
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

mouse = Mouse(usb_hid.devices)



btn1Pin = board.GP0
btn2Pin = board.GP5
btn3Pin = board.GP8
btn4Pin = board.GP1
btn5Pin = board.GP4
btn6Pin = board.GP7
btn7Pin = board.GP2
btn8Pin = board.GP3
btn9Pin = board.GP6

btn1 = digitalio.DigitalInOut(btn1Pin)
btn2 = digitalio.DigitalInOut(btn2Pin)
btn3 = digitalio.DigitalInOut(btn3Pin)
btn4 = digitalio.DigitalInOut(btn4Pin)
btn5 = digitalio.DigitalInOut(btn5Pin)
btn6 = digitalio.DigitalInOut(btn6Pin)
btn7 = digitalio.DigitalInOut(btn7Pin)
btn8 = digitalio.DigitalInOut(btn8Pin)
btn9 = digitalio.DigitalInOut(btn9Pin)

btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn3.direction = digitalio.Direction.INPUT
btn4.direction = digitalio.Direction.INPUT
btn5.direction = digitalio.Direction.INPUT
btn6.direction = digitalio.Direction.INPUT
btn7.direction = digitalio.Direction.INPUT
btn8.direction = digitalio.Direction.INPUT
btn9.direction = digitalio.Direction.INPUT

btn1.pull = digitalio.Pull.UP
btn2.pull = digitalio.Pull.UP
btn3.pull = digitalio.Pull.UP
btn4.pull = digitalio.Pull.UP
btn5.pull = digitalio.Pull.UP
btn6.pull = digitalio.Pull.UP
btn7.pull = digitalio.Pull.UP
btn8.pull = digitalio.Pull.UP
btn9.pull = digitalio.Pull.UP

timer = time.monotonic()

a=3

while True:
    
    btnValues = 9-(btn1.value+btn2.value+btn3.value+btn4.value+btn5.value+btn6.value+btn7.value+btn8.value+btn9.value)
    a = 3*btnValues
    
    
    btn5value=btn5.value    
    if btn5value == 0 and oldbtn5value == 1:
        mouse.click(Mouse.LEFT_BUTTON)
        timer = time.monotonic()
    oldbtn5value = btn5value
    if btn5value==0 and oldbtn5value == 0 and time.monotonic()-timer >=0.5:
        mouse.click(mouse.RIGHT_BUTTON)
        timer = time.monotonic()
        
    
    if btn2.value == 0:
        mouse.move(y=-a)
    
    if btn3.value == 0:
        mouse.move(y=-a)
        mouse.move(x=a)
    
    if btn6.value == 0:
        mouse.move(x=a)
        
    if btn9.value == 0:
        mouse.move(y=a)
        mouse.move(x=a)
    if btn8.value == 0:
        mouse.move(y=a)
        
    if btn7.value == 0:
        mouse.move(y=a)
        mouse.move(x=-a)
    
    if btn4.value == 0:
        mouse.move(x=-a)
        
    if btn1.value == 0:
        mouse.move(y=-a)
        mouse.move(x=-a)
