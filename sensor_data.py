#ghotty editor

readings = [0.85, 0.72, 0.48, 0.31, 0.12]

print(f"First reading: {readings[0]}")
print(f"fifth reading: {readings[4]}")
print(f"fourth reading: {readings[3]}")

print("===== SENSOR READINGS =====")
for reading in readings:
    print(f"Reading: {reading}m")

for reading in readings:
   if reading < 0.5:
      print(f"{reading} m > WARNING")
   else:
      print(f"{reading} m > SAFE")

## DAY 4 EXCERCISE
readings = [0.85, 0.72, 0.48, 0.31, 0.12]
def analyze_sensor_data(readings):
    #calculate average
    average = sum(readings) / len(readings)
    #find closest obstacle
    closest = min(readings)
    #create count warning
    warning_count = 0
    #decide robot action
    for reading in readings:
        if reading < 0.5: 
            warning_count = warning_count + 1

    if warning_count >= 3:
        decision = "STOP"
    else:
        decision = "CONTINUE"

    #return the results
    return average, closest, warning_count, decision 

average, closest, warning_count, decision = analyze_sensor_data(readings)

print("====== SENSOR ANALYSIS ======")
print(f"Average distance: {average} m")
print(f"Closest obstacle: {closest} m")
print(f"Warning count: {warning_count}")
print(f"Robot decision: {decision}")


