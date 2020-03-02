listdata = [[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]
#listdata = [[1], 2]

def flatten(data):
    r = []
    for i in data:
        if type(i) is list:
            for x in flatten(i):
                r.append(x)
        else:
            r.append(i)
    return r

print(flatten(listdata))