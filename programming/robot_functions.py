import math

def wheel_velocity(radius, rpm):
    frequency = rpm / 60
    velocity = 2*math.pi*radius*frequency

    return velocity

def robot_status(speed):
    if speed > 1.0:
        return "FAST"
    elif speed > 0.5:
        return "NORMAL"
    else:
        return "SLOW"

speed = wheel_velocity(0.05, 120)
status = robot_status(speed)

print(f"Robot velocity: {speed:.2f}m/s")
print("Robot status:", status)

try:
    distance = float(input("Enter distance: "))
    print(f"Distance: {distance} m")

except ValueError:
    print("Invalid sensor reading.")

