def time_converter(time):
    #replace this for solution
    s = time.split(':')
    #print(s)
    hour = int(s[0])
    minute = s[1]
    print("hour=" + str(hour) + ", minute=" + minute)

    surfix = "a.m."
    if hour >= 12:
        surfix = "p.m."
    if hour > 12:
        hour -= 12
    if hour == 0:
        hour = 12
        surfix = "a.m."

    result = str(hour) + ":" + minute + " " + surfix
    return result

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    assert time_converter('00:00') == '12:00 a.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")