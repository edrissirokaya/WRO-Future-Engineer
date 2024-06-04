#Contains Open Challenge Code



#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile



# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# initiallisation process
ev3 = EV3Brick()
Motor_Big = Motor(Port.D)
Motor_Small = Motor(Port.A)
UltraSonic_front = UltrasonicSensor(Port.S4)
UltraSonic_right = UltrasonicSensor(Port.S3)
UltraSonic_left = UltrasonicSensor(Port.S2)
GyroSensor_1 = GyroSensor(Port.S1)

# Write your program here.
Wheel_Turn = 0
GyroSensor_1.reset_angle(0)
Motor_Big.run(2000)

def Turn_Right():
    Motor_Small.run_target(2000, 40)


def Turn_Left():
    Motor_Small.run_target(2000, -40)


while Wheel_Turn < 16:

    if UltraSonic_right.distance() < 15:
        Turn_Left()
    if UltraSonic_left.distance() < 15:
        Turn_Right()
    if UltraSonic_right.distance() >= 100: 
        while Wheel_Turn < 16:
            if UltraSonic_front.distance() >= 30:
                Turn_Right()
            if GyroSensor_1.angle() >= 90 or GyroSensor_1.angle() <= -90 :
                GyroSensor_1.reset_angle(0)
                Turn_Left()
            if UltraSonic_right.distance() < 15:
                Turn_Left()
            if UltraSonic_left.distance() < 15:
                Turn_Right()

    if UltraSonic_left.distance() >= 100: 
        while Wheel_Turn < 16:
            if UltraSonic_front.distance() >= 30:
                Turn_Left()
            if GyroSensor_1.angle() >= 90 or GyroSensor_1.angle() <= -90 :
                GyroSensor_1.reset_angle(0)
                Turn_Right()
            if UltraSonic_right.distance() < 15:
                Turn_Left()
            if UltraSonic_left.distance() < 15:
                Turn_Right()
