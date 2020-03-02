friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
luck_numbers = [82, 4, 8, 15, 16, 23, 42]
data_set = [luck_numbers, friends]

print(friends)
print(friends[0])
print(len(friends))
print(friends[-2])
print(friends[1:])
print(friends[:2])
friends[1] = "Mike"
print(friends)
print(data_set)

# combine two lists
friends.extend(luck_numbers)
print(friends)
# append one elements at the end
friends.append(luck_numbers)
print(friends)
friends.insert(2, "Steve")
print(friends)
print("pop out")
friends.pop()
print(friends)
print(friends.count("Jim"))
luck_numbers.sort()
print(luck_numbers)
luck_numbers.reverse()
print(luck_numbers)

friends2 = friends.copy()
print(friends2)
friends.pop()
print(friends)
print(friends2)
