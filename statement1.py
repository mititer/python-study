is_male = True
is_male = False
is_tall = True

def f(flag):
    print("Parameter="+str(flag))

f(is_male)
if is_male and is_tall:
    print("I'm a man, and Tall.")
elif is_tall:
    print("Only is tall")
else:
    print("I'm not  man, nor tall")

if is_male:
    if is_tall:
        print("You are man, and tall")
    else:
        print("You are man, but not tall")
else:
    if is_tall:
        print("You are not a man, and tall")
    else:
        print("You are not a man, but not tall")
