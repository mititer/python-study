s = "ddvvrwwwrgggxxddddd"

def long_repeat(data):
    result = {}
    previous_ch = data[0]
    # go through and do statistics
    for i in range(len(data)):
        n = 0
        v = result.get(data[i])
        if v:
            if i > 0 and data[i-1] == data[i]:
                n = v + 1
            else:
                n = v
        else:
            n = 1
        result.update({data[i]: n})
    # get the max
    m = 0
    for (k, v) in result.items():
        if v > m:
            m = v
    return m

s = ''
s = 'abababaab'
print(long_repeat(s))