from DBDynamics import Bee
import time
m = Bee('/dev/ttyUSB0')

for axis in range(0,64):
    m.setHomingMode(axis)
    time.sleep(0.1)

m.stop()