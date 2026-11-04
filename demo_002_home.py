from DBDynamics import Bee

m = Bee('/dev/ttyUSB0')
# m = Bee('COM3') # WINDOWS用户

# First Homing Sequence
input("开始第一回零,按回车开始")
for mid in range(0, 4):
    m.setHomingDirection(mid, 1)
    m.setHomingLevel(mid, 0)
    m.setTargetVelocity(mid, 500)
    m.setHomingMode(mid)
for mid in range(0, 4):
    m.waitTargetPositionReached(mid)
print("第一回零结束")

# Move motors to a specific position
input("运动一点点,按回车开始")
for mid in range(0, 4):
    m.setAccTime(mid, 200)
    m.setTargetVelocity(mid, 1000)
    m.setPositionMode(mid)
    m.setTargetPosition(mid, 51200/2)
for mid in range(0, 4):
    m.waitTargetPositionReached(mid)

# Second Homing Sequence
input("开始第二回零,按回车开始")
for mid in range(0, 4):
    m.setHomingDirection(mid, 1)
    m.setHomingLevel(mid, 0)
    m.setTargetVelocity(mid, 500)
    m.setHomingMode(mid)
for mid in range(0, 4):
    m.waitTargetPositionReached(mid)
print("第二回零结束")
# time.sleep(1)
m.stop()
