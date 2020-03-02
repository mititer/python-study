def say_hi(name, age):
    print("Hi " + name + "!. You are " + str(age))
    name = "CHANGED!!!"
    print(name)

name = "Mike"
age = 20
print(name )
say_hi(name, age)
name = "Tom"
say_hi(name, age)
print(name)
