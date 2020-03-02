monthConversations = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

print(monthConversations)
print(monthConversations['Dec'])
print(monthConversations.get("NoV", "AAA"))

datalist = {
    'a': 1
}
print(datalist.get('a'))
if datalist.get('b'):
    print("key=b is found")
else:
    print("key=b is NOT found")
    datalist.update({'b': 1})
r = datalist.get('b')
print(r)

for (k,v) in datalist.items():
    print("key=" + k + ", value=" + str(v))
