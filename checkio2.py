def checkio(data_string: str) -> bool:
    #replace this for solution
    print("checking " + data_string)
    length = len(data_string)
    if length < 10:
        print("ERROR: length=" + str(length) + " is less than 10.")
        return False;
    # check at least one digit
    has_one_digit = False
    i = 0
    while not has_one_digit and i < length:
        if data_string[i].isdigit():
            has_one_digit = True
        i += 1
    if not has_one_digit:
        print("ERROR: no digit number.")
        return False

    # check one uppercase letter
    has_one_uppercase = False
    i = 0
    while not has_one_uppercase and i < length:
        if data_string[i].isupper():
            has_one_uppercase = True
        i += 1
    if not has_one_uppercase:
        print("ERROR: no uppercase letter.")
        return False

    # check one lowercase letter
    has_one_lowercase = False
    i = 0
    while not has_one_lowercase and i < length:
        if data_string[i].islower():
            has_one_lowercase = True
        i += 1
    if not has_one_lowercase:
        print("ERROR: no lowercase letter.")
        return False

    # check only_latin_digit letter
    only_latin_digit = True
    i = 0
    while only_latin_digit and i < length:
        if not data_string[i].isdigit() and not data_string[i].isupper() and not data_string[i].islower():
            only_latin_digit = False
            print("ERROR: invalid index=" + str(i) + ", value=" + data_string[i])
        i += 1
    if not only_latin_digit:
        print("ERROR: not only latin and digit letter.")
        return False

    return True

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")