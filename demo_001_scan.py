from DBDynamics import Bee

# Create a Bee instance by specifying the serial port
# For Linux/Mac users, use '/dev/ttyUSB0' or similar
m = Bee('/dev/ttyUSB0')
# m = Bee('COM3') # For Windows users

# Scan for connected Bee devices on the bus
# Returns a list of device IDs found
a = m.scanDevices()
# Print the number of devices found and their IDs
print(len(a), a)

# Close the serial connection
m.stop()
