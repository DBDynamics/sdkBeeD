from DBDynamics import Bee

# Initialize Bee motor controller on USB port
m = Bee('/dev/ttyUSB0')

# Change the ID of the motor from 0 to 1
# First parameter (0) is the current ID
# Second parameter (1) is the new ID
m.changeID(0, 1)

# Stop the motor and close the connection
m.stop()
