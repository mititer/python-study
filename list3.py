data = [3, 5, 4, 6, 2, 2, 6, 4, 4, 4]

def frequency_sort(data):
    dict = {}
    result = []

    # count the frequency and save in dict dictionary
    for item in data:
        print(item)
        n = data.count(item)
        if not dict.get(item):
            dict.update({item: n})

    # sort the dictionary
    dict = sorted(dict.items(), key=lambda item:item[1], reverse=True)

    # generate the result
    for (k, v) in dict:
        for i in range(v):
            result.append(k)

    return result

print(frequency_sort(data))