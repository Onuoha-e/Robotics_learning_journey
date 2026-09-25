
import math
wheel_rd = 0.08
wheel_rpm = 180

frq = wheel_rpm/60

velocity = 2*math.pi*wheel_rd*frq

print("=== ROBOT WHEEL CALCULATOR ===")
print("Wheel radius:", wheel_rd, "m")
print("Wheel_speed:", wheel_rpm, "RPM")
print("Robot velocity:", round(velocity, 2), "m/s")

