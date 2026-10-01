readings = [0.85, 0.72, 0.48, 0.31, 0.12]

warning_count = 0

for reading in readings:
   if reading <= 0.5:
       warning_count = warning_count + 1
       #shortform= warning_count += 1
print("Warning count:", warning_count)

def count_warnings(readings):
    warning_count = 0

    for reading in readings:
        if reading <= 0.5:
            warning_count += 1

    return warning_count

warnings = count_warnings(readings)

print("Warning count:", warnings)

def robot_decision(warning_count):

    if warning_count == 0:
        return "CONTINUE"
    elif warning_count <= 2:
        return "CAUTION"
    else:
        return "STOP"

decision = robot_decision(warnings)
print("Robot decision:", decision)
