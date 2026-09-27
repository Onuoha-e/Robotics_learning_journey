print("###### DAY 2 CHALLENGE")
readings = [0.85, 0.72, 0.48, 0.31, 0.12]

for reading in readings:
    print("Reading:", reading, "m")

for reading in readings:
    
  if reading > 1.0:
       print("MOVE FAST")
  elif reading > 0.5:
       print("Sensor:", reading, "m", ">", "MOVE")
  elif reading > 0.2:
       print("Sensor:", reading, "m", ">", "SLOW DOWN")
  else:
       print("Sensor:", reading, "m", ">","STOP") 

print("-----Number of readings, Average distance, Minimum distance, Maximum distance")

print("##### Number of readings")
print("Number of readings:", len(readings))
average = sum(readings) / len(readings)
print("Average distance:", average)
print("Minimum distance:", min(readings))
print("Maximum distance:", max(readings))

print("###### BONUS CHALLENGE")
readings = [0.85, 0.72, 0.48, 0.31, 0.12]

def robot_response(reading):
  
    if reading > 1.0:
        return f"Sensor: {reading} m > MOVE FAST"

    elif reading > 0.5:
        return f"Sensor: {reading} m > MOVE"

    elif reading > 0.2:
        return f"Sensor: {reading} m > SLOW DOWN"

    else:
        return f"Sensor: {reading} m > STOP"

for reading in readings:
    print(robot_response(reading))
