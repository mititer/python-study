tm = "07:00"
tm = "12:00"
tm = "12:15"
tm = "01:15"

def get_angle(t: str) -> float:
    s = t.split(':')
    hour = int(s[0])
    minute = int(s[1])

    if hour < 6 or ( hour == 18 and minute > 0):
        print("I don't see the sun!")
        return -1

    return round(((hour - 6) * 60 + minute) * (180 / (12 * 60)), 2)

print(get_angle(tm))