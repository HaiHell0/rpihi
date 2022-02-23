# CIT 381 - Spring 2022
# Authour: Hai Hoang
# Created: February 2nd, 2022
# Led on Gpio 17, Button on Gprio 27, press button for LED to blink 5 times

from gpiozero import Button
from gpiozero import LED
from gpiozero import MotionSensor
import time

# Set up Arm Button at gpio17
armButton = Button(17, bounce_time=0.25)

# Set up Alarm LED at gpio26
alarmLed = LED(17, active_high=False)

# Set up Armed LEd at gpio19
armedLed = LED(19, active_high=False)

# Set up Reed Switch at gpio20
reedSwitch = Button(20, bounce_time=0.25)

# Set up motion sensor at gpio21

motion = MotionSensor(21)

armed = False

alarm = False

def initialize():
    alarmLed.off()
    armedLed.off()

def armButtonPress(armed):
    if armed: 
        armed = False
        armedLed.off()
        print("armedLed Off")
    else: 
        armed = True
        armedLed.on()
        print("armedLed On")

def motionSensed(armed):
    if armed:
        alarm = True
        alarmLed.on()
        

def motionNotSensed():
    if alarm:
        alarm = False
        alarmLed.off()


def sendMessage(Message):
    print(Message)

def main():
    armedLed.when_pressed = armButtonPress
    motion.when_no_motion = motionNotSensed
    motion.when_motion = motionSensed
main()