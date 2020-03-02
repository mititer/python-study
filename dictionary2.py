datalist = {
    'a': 1,
    'b': 3,
    'c': 3,
    'd': 2,
}

result=()
for item in datalist.items():
    #print(item)
    #print(item[0])
    #print(item[1])
    if not result:
        result = item
    else:
        if item[1] > result[1]:
            result = item

print(result)
