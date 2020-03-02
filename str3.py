first = 'John'
last = 'Smith'
age = 50

class Man:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        return

    def __str__(self):
        return f'{first} {last} {age} years old'

# format string
msg = f'{first} [{last}] is a coder who is {age} years old'
print(msg)
# no format
msg = '{first} [{last}] is a coder who is {age} years old'
print(msg)

man = Man(first, last, age)
msg = f'[{man}] is a coder'
print(msg)