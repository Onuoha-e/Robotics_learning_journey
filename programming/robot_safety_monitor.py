readings = [0.85, 0.72, 0.48, 0.31, 0.12]

def calculate_average(readings):

    average = sum(readings) / len(readings)
    return average

def count_warnings(readings):
    warning_count = 0

    for reading in readings:
        if reading <= 0.5:
            warning_count += 1

    return warning_count

def robot_decision(warning_count):

     if warning_count == 0:
         return "CONTINUE"
     elif warning_count <= 2:
         return "CAUTION"
     else:
         return "STOP"

average_distance = calculate_average(readings)
closest = min(readings)
warning_count = count_warnings(readings)
decision = robot_decision(warning_count) 

print("===== ROBOT SAFETY MONITOR =====")
print(f"Average distance: {average_distance} m")
print(f"Closest obstacle: {closest} m")
print(f"Warning count: {warning_count}")
print(f"Robot decision: {decision}")
