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

## Functions per Key
#volume up      |     x       |     x
#pause/skip etc | open app    |     x
#volume down    | switch app  |     x


#void setup()

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

keyboard = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

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

btn1ontime = time.monotonic()
btn2ontime = time.monotonic()
btn3ontime = time.monotonic()
btn4ontime = time.monotonic()
btn5ontime = time.monotonic()
btn7ontime = time.monotonic()
toggle1 = 1 
toggle7 = 1
toggleMode1 = 1
toggleMode2 = 1
btn4state = 0 # initial btn 4 state
btn5state = 0 # initial btn 4 state

## CHANGE THESE VARIABLES ##
pushDelay = 0.5   #Time (seconds) between press and hold for volume up/down
btnPress = 0
mode = 1
# LED Startup Blink
# 
# while n<12:
#     led.value = (ledToggle+1)/2
#     ledToggle = -ledToggle
#     n=n+1
#     time.sleep(0.1)

def modeLED(int):
    modeLEDReference = time.monotonic()
    n=1
    ledToggle = 1
    led.value = True
    time.sleep(0.7)
    led.value = False
    time.sleep(0.3)
    while n<int*2:
        led.value = (ledToggle+1)/2
        ledToggle = -ledToggle
        n=n+1
        time.sleep(0.1)
    led.value = False
    time.sleep(0.1)


#void loop()
while True:
    
    
    
    

    
    
    
    
    
    
    
    
    if mode == 1:
        
        #LED display btn press
        btnPress = btn1.value+btn2.value+btn3.value+btn4.value+btn5.value+btn6.value+btn7.value+btn8.value+btn9.value
        if btnPress <9:
            led.value = True
        else:
            led.value = False
        
        
        #Play/Pause, skip Forward, Previous track   Rising Edge (Button 4) 
        btn4value = btn4.value

        if btn4state == 2 and time.monotonic()-btn4ontime < pushDelay and btn4value == 0 and oldbtn4value == 1:
            btn4state = 3
            btn4ontime = time.monotonic()
            
        if btn4state == 1 and time.monotonic()-btn4ontime < pushDelay and btn4value==0 and oldbtn4value == 1:
            btn4state = 2
            btn4ontime = time.monotonic()
            
        if btn4state == 0 and btn4value == 0 and oldbtn4value == 1 :
            btn4state = 1
            btn4ontime = time.monotonic()
        
        if time.monotonic()-btn4ontime > pushDelay:
            if btn4state == 1:
                cc.send(ConsumerControlCode.PLAY_PAUSE) #1 press is play/pause
            if btn4state == 2:
                cc.send(ConsumerControlCode.SCAN_NEXT_TRACK) #2 presses is skip track
            if btn4state == 3:
                cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK) #3 presses is previous track
            btn4state = 0
        oldbtn4value = btn4value
        
        #Volume Increase   Rising Edge + delayed hold (Button 1)
        btn1value=btn1.value
        if btn1value == 0 and oldbtn1value == 1:
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            btn1ontime = time.monotonic()
        if time.monotonic()-btn1ontime>=pushDelay and btn1value == 0 and oldbtn1value == 0:
            if toggle1 == 1:
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            toggle1 = -toggle1
        oldbtn1value = btn1value
        
        #Volume Decrease   Rising Edge + delayed hold (Button 7)
        btn7value=btn7.value
        if btn7value == 0 and oldbtn7value == 1:
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
            btn7ontime = time.monotonic()
        if time.monotonic()-btn7ontime>=pushDelay and btn7value == 0 and oldbtn7value == 0:
            if toggle7 == 1:
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
            toggle7 = -toggle7
        oldbtn7value = btn7value
        
        
        #WINDOWS+1/2/3/4 etc   Rising Edge (Button 5)
        btn5value = btn5.value
        if btn5state == 3 and time.monotonic()-btn5ontime < pushDelay and btn5value == 0 and oldbtn5value == 1:
            btn5state = 4
            btn5ontime = time.monotonic()

        if btn5state == 2 and time.monotonic()-btn5ontime < pushDelay and btn5value == 0 and oldbtn5value == 1:
            btn5state = 3
            btn5ontime = time.monotonic()
            
        if btn5state == 1 and time.monotonic()-btn5ontime < pushDelay and btn5value==0 and oldbtn5value == 1:
            btn5state = 2
            btn5ontime = time.monotonic()
            
        if btn5state == 0 and btn5value == 0 and oldbtn5value == 1 :
            btn5state = 1
            btn5ontime = time.monotonic()
        
        if time.monotonic()-btn5ontime > pushDelay:
            keyboard.release_all()
            if btn5state == 1:
                keyboard.press(Keycode.GUI, Keycode.ONE)
            if btn5state == 2:
                keyboard.press(Keycode.GUI, Keycode.TWO)
            if btn5state == 3:
                keyboard.press(Keycode.GUI, Keycode.THREE)
            if btn5state == 4:
                keyboard.press(Keycode.GUI, Keycode.FOUR)
            
            btn5state = 0
        oldbtn5value = btn5value
        
        #Ctrl+Tab   Rising Edge (Button 8)  5 TO WINDOWS+1/2/3/4 ETC (MULTIPLE PRESSES MEAN DIFFERENT APPLICATIONS) 
        btn8value=btn8.value
        
        if btn8value == 0 and oldbtn8value == 1:
            keyboard.send(Keycode.LEFT_ALT, Keycode.TAB)
            #release_all()
        oldbtn8value = btn8value
        
        
        
        
    if mode == 2:
        
        
        #LED display btn press MODE 2
        btnPress = btn1.value+btn2.value+btn3.value+btn4.value+btn5.value+btn6.value+btn7.value+btn8.value+btn9.value
        if btnPress <9:
            led.value = False
        else:
            led.value = True
        
        #Flip (button 4)
        btn4value=btn4.value
        if btn4value == 0 and oldbtn4value == 1:
            keyboard.send(Keycode.CONTROL, Keycode.EIGHT)
        oldbtn4value = btn4value
        
        #Top (Button 5)
        btn5value=btn5.value
        if btn5value == 0 and oldbtn5value == 1:
            keyboard.send(Keycode.CONTROL, Keycode.FIVE)
        oldbtn5value = btn5value
        
        #Isometric (Button 6)
        btn6value=btn6.value
        if btn6value == 0 and oldbtn6value == 1:
            keyboard.send(Keycode.CONTROL, Keycode.SEVEN)
        oldbtn6value = btn6value
        
        #Front (Button 8)
        btn8value=btn8.value
        if btn8value == 0 and oldbtn8value == 1:
            keyboard.send(Keycode.CONTROL, Keycode.ONE)
        oldbtn8value = btn8value
    
        #Right (Button 9)
        btn9value=btn9.value
        if btn9value == 0 and oldbtn9value == 1:
            keyboard.send(Keycode.CONTROL, Keycode.FOUR)
        oldbtn9value = btn9value
    
    
    #    Select Mode 1
    btn2value=btn2.value
    if btn2value == 0 and oldbtn2value == 1:
        #btn 2 mode 1 to be implemented        
        btn2ontime = time.monotonic()
    if time.monotonic()-btn2ontime>=pushDelay and btn2value == 0 and oldbtn2value == 0:
        if toggleMode1 == 1:
            mode = 1
            modeLED(1)
        toggleMode1 = -toggleMode1
    oldbtn2value = btn2value
    
#    Select Mode 2        
    btn3value=btn3.value
    if btn3value == 0 and oldbtn3value == 1:
        #btn 2 mode 1 buton to be implemented
        btn3ontime = time.monotonic()
    if time.monotonic()-btn3ontime>=pushDelay and btn3value == 0 and oldbtn3value == 0:
        if toggleMode2 == 1:
            mode = 2
            modeLED(2)
        toggleMode2 = -toggleMode2
    oldbtn3value = btn3value
    
    time.sleep(0.01)

    

