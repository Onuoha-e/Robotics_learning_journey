import math

wheel_rd  = 0.075
wheel_rpm = 150

frq = wheel_rpm / 60
circumference = 2*math.pi*wheel_rd
velocity = circumference*frq
t = 60
d = velocity*t

print("Wheel circumference:", round(circumference, 2))
print("Wheel rotations per second:", wheel_rpm, "/sec")
print("Linear velocity:", round(velocity, 2), "m/s")
print("Distance travelled:",round(d, 2), "m")



