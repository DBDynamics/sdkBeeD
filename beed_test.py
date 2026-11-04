
from DBDynamics import Bee
import time
m = Bee('/dev/ttyUSB0')
# m = Bee('COM3') # For Windows users

for mid in range(0, 10):
    m.setTargetVelocity(mid, 200)
    m.setAccTime(mid, 500)
    m.setHomingLevel(mid, 0)
    m.setHomingDirection(mid, 1)
    m.setCurrentBase(mid, 500)
    m.setCurrentP(mid, 3)
    m.setCurrentN(mid, 2)
    m.setPositionMode(mid)
    time.sleep(0.5)
time.sleep(1)
print("start 1st homing")
for mid in range(0, 10):
    m.setHomingMode(mid)
for mid in range(0, 10):
    m.waitTargetPositionReached(mid)
print("move a bit")
for mid in range(0, 10):
    m.setTargetPosition(mid, 12800)
for mid in range(0, 10):
    m.waitTargetPositionReached(mid)
print("start 2nd homing")
for mid in range(0, 10):
    m.setHomingMode(mid)
for mid in range(0, 10):
    m.waitTargetPositionReached(mid)
print("homing done")

while True:
    input("press enter to turn 180")
    for mid in range(0, 10):
        m.setTargetPosition(mid, 25600)
    for mid in range(0, 10):
        m.waitTargetPositionReached(mid)

    input("press enter to turn back")
    for mid in range(0, 10):
        m.setTargetPosition(mid, 0)
    for mid in range(0, 10):
        m.waitTargetPositionReached(mid)


m.stop()