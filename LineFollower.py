# VEX V5 Python Project
import sys
import vex
from vex import *
import motor_group
import drivetrain
import smartdrive

#region config
brain    = vex.Brain()
motor_r  = vex.Motor(vex.Ports.PORT1, vex.GearSetting.RATIO18_1, False)
motor_l = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, True)
sonar1  = vex.Sonar(brain.three_wire_port.a)
lineFollower1 = vex.Line(brain.three_wire_port.d)
lineFollower2 = vex.Line(brain.three_wire_port.h)
lineFollower3 = vex.Line(brain.three_wire_port.g)
bumperR = vex.Bumper(brain.three_wire_port.e)
bumperL = vex.Bumper(brain.three_wire_port.f)
#endregion config

black_value = 55
drive_dist = 1
the_speed = 20
stop_dist = 6.0
turn_value = the_speed

# Start
def main():
    
    while True:
        _offset = 0

        if (bumperR.pressing() or bumperL.pressing()):
            return
        
        if (sonar1.distance(vex.DistanceUnits.IN) <= stop_dist and sonar1.distance(vex.DistanceUnits.IN) > 0):
            motor_r.stop()
            motor_l.stop()
            continue
        
        if (lineFollower1.value() < black_value and \
        lineFollower2.value() < black_value and \
        lineFollower3.value() < black_value):
            motor_r.spin(vex.DirectionType.FWD, the_speed, vex.VelocityUnits.PCT)
            motor_l.spin(vex.DirectionType.FWD, -the_speed, vex.VelocityUnits.PCT)
            continue
        elif (lineFollower2.value() >= black_value):
            _offset = 0
        else:
            if (lineFollower1.value() >= black_value):
                _offset = -turn_value
            else:
                _offset = turn_value

        motor_r.spin(vex.DirectionType.FWD, the_speed + _offset, vex.VelocityUnits.PCT)
        motor_l.spin(vex.DirectionType.FWD, the_speed - _offset, vex.VelocityUnits.PCT)
        

main()