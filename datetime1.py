datetime='19:21'

s = datetime.split(':')
print(s)
hour = int(s[0])
minute = int(s[1])
print("hour=" + str(hour) + ", minute=" + str(minute))

surfix = "am"
if hour >= 12:
    surfix = "pm"
if hour > 12:
    hour -= 12

result = str(hour) + ":" + str(minute) + " " + surfix
print(result)
