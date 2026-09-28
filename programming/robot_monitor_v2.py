readings = [0.85, 0.72, 0.48, 0.31, 0.12]

def calculate_average(readings):

    average = sum(readings) / len(readings)
    return average

def robot_response(distance):
    if distance > 1.0:
        return "MOVE FAST"
    elif distance > 0.5:
        return "MOVE"
    elif distance > 0.2:
        return "SLOW DOWN"
    else:
        return "STOP"

def monitor_robot(readings):
    for reading in readings:
        response = robot_response(reading)
        print(f"Sensor: {reading} m > {response}")

print("===== ROBOT SENSOR MONITOR =====")
monitor_robot(readings)
print("===== SENSOR STATISTICS =====")
average = calculate_average(readings)

print(f"Average reading: {average} ")
print(f"Number of readings: {len(readings)}")
print(f"Minimum reading: {min(readings)} m")
print(f"Maximum reading: {max(readings)} m")
