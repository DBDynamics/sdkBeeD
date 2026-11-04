import time

from DBDynamics import Bee

m = Bee('/dev/ttyUSB0')

base_current = 500
parameter_p = 3
parameter_n = 2
homing_velocity = 200
mid = 1

m.setCurrentBase(mid, base_current)
m.setCurrentP(mid, parameter_p)
m.setCurrentN(mid, parameter_n)
m.setTargetVelocity(mid, homing_velocity)
m.setHomingDirection(mid, 1)
m.setHomingLevel(mid, 0)
m.setInterpolationPositionMode(mid)

time.sleep(3)

m.saveParameters(mid)
time.sleep(0.5)
m.stop()
