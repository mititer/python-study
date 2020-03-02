def checkio(text: str) -> str:

    #replace this for solution
    datalist = {}
    for s in text:
        if s.isupper() or s.islower():
            ch = s.lower()
            r = datalist.get(ch)
            if not r:
                r = 1
            datalist.update({ch: (r + 1)})

    print(datalist)
    result=()
    for item in datalist.items():
        if not result:
            result = item
        else:
            if item[1] > result[1]:
                result = item
            if item[1] == result[1]:
                if item[0] < result[0]:
                    result = item
    return result[0]


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")