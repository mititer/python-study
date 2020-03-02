data = [1, 2, 3, 1, 3, 4, 5, 6, 5, 4]

def filter(data):
    result = []
    for index in range(len(data)):
        if data.count(data[index]) > 1:
            result.append(data[index])
    return result

print(filter(data))