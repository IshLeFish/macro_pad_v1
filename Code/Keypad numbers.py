import time
import digitalio
import board
import usb_hid

#keyboard inputs
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
#Consumer Control Devices (volume control etc. )
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode 



##Pin numbers according to PCB+Pico
# 0 | 5 | 8
# 1 | 4 | 7
# 2 | 3 | 6

##Keyboard numbers as referenced in code
# 1 | 2 | 3
# 4 | 5 | 6
# 7 | 8 | 9


##Setup
#set pin numbers
btn1Pin = board.GP0
btn2Pin = board.GP5
btn3Pin = board.GP8
btn4Pin = board.GP1
btn5Pin = board.GP4
btn6Pin = board.GP7
btn7Pin = board.GP2
btn8Pin = board.GP3
btn9Pin = board.GP6

#Identify keyboard and cc(consumer control) objects to be referred to later on
keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)
#Identify LED object
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

#Identify buttons as objects
btn1 = digitalio.DigitalInOut(btn1Pin)
btn2 = digitalio.DigitalInOut(btn2Pin)
btn3 = digitalio.DigitalInOut(btn3Pin)
btn4 = digitalio.DigitalInOut(btn4Pin)
btn5 = digitalio.DigitalInOut(btn5Pin)
btn6 = digitalio.DigitalInOut(btn6Pin)
btn7 = digitalio.DigitalInOut(btn7Pin)
btn8 = digitalio.DigitalInOut(btn8Pin)
btn9 = digitalio.DigitalInOut(btn9Pin)

#Specify pins as inputs (not outputs)
btn1.direction = digitalio.Direction.INPUT
btn2.direction = digitalio.Direction.INPUT
btn3.direction = digitalio.Direction.INPUT
btn4.direction = digitalio.Direction.INPUT
btn5.direction = digitalio.Direction.INPUT
btn6.direction = digitalio.Direction.INPUT
btn7.direction = digitalio.Direction.INPUT
btn8.direction = digitalio.Direction.INPUT
btn9.direction = digitalio.Direction.INPUT


#use internal pullup resistors to pull button pins up
btn1.pull = digitalio.Pull.UP
btn2.pull = digitalio.Pull.UP
btn3.pull = digitalio.Pull.UP
btn4.pull = digitalio.Pull.UP
btn5.pull = digitalio.Pull.UP
btn6.pull = digitalio.Pull.UP
btn7.pull = digitalio.Pull.UP
btn8.pull = digitalio.Pull.UP
btn9.pull = digitalio.Pull.UP











n=1
ledToggle = -1
# LED Startup Blink
while n<12:
    led.value = (ledToggle+1)/2
    ledToggle = -ledToggle
    n=n+1
    time.sleep(0.1)





#void loop()
while True:
    
    btn1value=btn1.value
    if btn1value == 0 and oldbtn1value == 1:
        keyboard.send(Keycode.EIGHT)
    oldbtn1value = btn1value
    
    btn2value=btn2.value
    if btn2value == 0 and oldbtn2value == 1:
        print("Switch 2 is operational")
    oldbtn2value = btn2value
    
    btn3value=btn3.value
    if btn3value == 0 and oldbtn3value == 1:
        print("Switch 3 is operational")
    oldbtn3value = btn3value
    
    btn4value=btn4.value
    if btn4value == 0 and oldbtn4value == 1:
        print("Switch 4 is operational")
    oldbtn4value = btn4value
    
    btn5value=btn5.value
    if btn5value == 0 and oldbtn5value == 1:
        print("Switch 5 is operational")
    oldbtn5value = btn5value
    
    btn6value=btn6.value
    if btn6value == 0 and oldbtn6value == 1:
        print("Switch 6 is operational")
    oldbtn6value = btn6value

    btn6value=btn6.value
    if btn6value == 0 and oldbtn6value == 1:
        print("Switch 6 is operational")
    oldbtn6value = btn6value

    btn7value=btn7.value
    if btn7value == 0 and oldbtn7value == 1:
        print("Switch 7 is operational")
    oldbtn7value = btn7value

    btn8value=btn8.value
    if btn8value == 0 and oldbtn8value == 1:
        print("Switch 8 is operational")
        keyboard.send(Keycode.F12)
        
    oldbtn8value = btn8value
    
    btn9value=btn9.value
    if btn9value == 0 and oldbtn9value == 1:
        print("Switch 9 is operational")
    oldbtn9value = btn9value





    time.sleep(0.01)

    



