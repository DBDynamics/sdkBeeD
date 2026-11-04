from DBDynamics import Bee

# Initialize Bee controller - choose the appropriate port
m = Bee('/dev/ttyUSB0')
# m = Bee('COM3') # WINDOWS用户

# Initialize position array and constants
tp = []
offset = 1000  # Base offset for all positions
k = 51200 / 360.0  # Conversion factor from degrees to steps (51200 steps = 360 degrees)
for axis in range(0, 4):
    tp.append(0)


def mov(p0, p1, p2, p3):
    """
    Move all 4 axes to specified positions in degrees
    Parameters:
        p0, p1, p2, p3: Target positions in degrees for each axis
    """
    # Convert degrees to steps and store in position array
    tp[0] = p0 * k
    tp[1] = p1 * k
    tp[2] = p2 * k
    tp[3] = p3 * k
    
    # Set target position for each motor (adding offset)
    for mid in range(0, 4):
        m.setTargetPosition(mid, tp[mid]+offset)
    
    # Wait for all motors to reach their positions
    for mid in range(0, 4):
        m.waitTargetPositionReached(mid)


# Execute a sequence of movements
mov(0, 0, 0, 0)          # Move all axes to home position
mov(90, 90, 90, 90)      # Move all axes to 90 degrees
mov(-90, -90, -90, -90)  # Move all axes to -90 degrees
mov(90, -90, 90, -90)    # Move axes in alternating +90/-90 pattern
mov(-90, 90, -90, 90)    # Move axes in opposite alternating pattern
mov(0, 0, 0, 0)          # Return to home position

# Stop the controller
m.stop()
