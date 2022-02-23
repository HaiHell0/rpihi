# CIT 381 - Spring 2022
# Authour: Hai Hoang
# Created: February 2nd, 2022
# Led on Gpio 17, Button on Gprio 27, press button for LED to blink 5 times
from sendEmail import *
from gpiozero import Button
from gpiozero import LED
from gpiozero import MotionSensor
import time

# Set up Arm Button at gpio17
armButton = Button(17, bounce_time=0.25)

# Set up Alarm LED at gpio26
alarmLed = LED(26, active_high=False)

# Set up Armed LEd at gpio19
armedLed = LED(19, active_high=False)

# Set up Reed Switch at gpio20
reedSwitch = Button(20, bounce_time=0.25)

# Set up motion sensor at gpio21

motion = MotionSensor(21)

armed = False

alarm = False

switch = False


def initialize():
    alarmLed.off()
    armedLed.off()

def armButtonPress():
    global armed
    global alarm
    if armed: 
        armed = False
        armedLed.off()
        alarm = False
        alarmLed.off()
        print("armedLed Off")
    else: 
        armed = True
        armedLed.on()
        print("armedLed On")
        switch = not reedSwitch.is_pressed
        if switch:
            print("Reed Switch On")
            alarmLed.on()
            alarm = True

def motionSensed():
    global armed
    global alarm
    if armed and alarm==False:
        print("Motion is detected")
        sendEmail("8599134906@mailmymobile.net","LAB4motionSensor","Motion was sensed")
        alarm = True
        alarmLed.on()
        

def motionNotSensed():
    global armed
    global alarm
    if alarm and switch==False:
        alarm = False
        alarmLed.off()
        
def reedClosed():
    global armed
    global alarm
    global switch
    print("reed switch is closed")
    if alarm and switch:
        alarm = False
        switch = False
        alarmLed.off()

def reedOpen():
    global armed
    global alarm
    global switch
    if armed and switch==False:
        print("Alarm")
        print("Reed Switch Open")
        sendEmail("8599134906@mailmymobile.net","LAB4motionSensor","Reed switch was opened")
        alarm = True
        switch = True
        alarmLed.on()
    
    
def main():
    global armed
    global alarm
    global switch

    armButton.when_pressed = armButtonPress
    motion.when_no_motion = motionNotSensed
    motion.when_motion = motionSensed
    reedSwitch.when_held = reedClosed
    reedSwitch.when_released = reedOpen

    time.sleep(0.01)
main()