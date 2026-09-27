import math
robot_name = "PARC"
wheel_radius = 0.075
wheel_rpm = 150
number_of_wheels = 4
robot_active = True

rpm = 150
rotations_per_second = rpm / 60

print("Rotations per second:", round(rotations_per_second, 2))
print(robot_name)
print(wheel_radius)
print(wheel_rpm)
print(number_of_wheels)
print(robot_active)

print("###### NEW IF/ELSE PROGRAM")
distance  = 0.45
if distance > 0.5:
   print("Move")
else:
   print("Stop")

print("###### MULTIPLE CONDITIONS")

distance = 5.0

if distance > 1.0:
    print("safe - move fast")
elif distance > 0.5:
    print("caution - move")
elif distance > 0.2:
    print("warning - slow down")
else:
    print("DANGER - STOP")

print("##### LOOPS")
distances = [1.2, 0.8, 0.6, 0.3, 0.15]

for distance in distances:
    print("Distance:", distance)

for distance in distances:

    if distance > 0.5:
       print("move")
    else:
       print("stop")

print("###### FUNCTIONS")

def obstacle_response(distance):

    if distance > 1.0:
        return "MOVE FAST"
    elif distance > 0.5:
        return "MOVE"
    elif distance > 0.2:
        return "SLOW DOWN"
    else:
        return "STOP"
print(obstacle_response(1.5))
print(obstacle_response(0.7))
print(obstacle_response(0.3))
print(obstacle_response(0.1))

print("###### LISTS")
temperatures = [32.5, 33.1, 34.0, 35.2]
print(temperatures[0])
print(temperatures[1])
print(temperatures[-1])

for temperature in temperatures:
    print("Temperature:", temperature)
average = sum(temperatures) / len(temperatures)

print("Average temperatures:", average)

print("##### DICTIONARIES")
#structures infomation.

robot = {
     "name": "PARC",
     "wheel_radius": 0.075,
     "battery_voltage": 12.0,
     "active": True
}
print(robot["name"])
print(robot["wheel_radius"])
print(robot["battery_voltage"])

robot["battery_voltage"] = 11.7
print(robot["battery_voltage"])

