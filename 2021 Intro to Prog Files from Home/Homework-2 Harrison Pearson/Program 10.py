#Time problem solved using minutes method
startTime = 6 * 60 + 52
easyPace = (8 + 15/60) * 2
tempoPace = (7 + 12/60) * 3
totalMinutes = startTime + easyPace + tempoPace

hourSpec = totalMinutes // 60
minuteSpec = totalMinutes % 60
minuteInt = int(minuteSpec)
secondSpec = (minuteSpec - minuteInt)*60
secondSpec = int(secondSpec)

print("Hours")
print(hourSpec)
print("Minutes")
print(minuteInt)
print("Seconds")
print(secondSpec)
